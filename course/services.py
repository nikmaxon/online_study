import stripe
from rest_framework import serializers
from config.settings import STRIPE_TOKEN
from course.models import Course, Lesson, Payment


def get_session_of_payment(
        self,
        success_url: str = 'https://example.com/success',
) -> stripe.checkout.Session:
    stripe.api_key = STRIPE_TOKEN

    amount = self.request.data.get('amount')
    paid_lesson_id = self.request.data.get('paid_lesson')
    paid_course_id = self.request.data.get('paid_course')

    payment_obj = get_id_of_payment_obj(paid_lesson_id, paid_course_id)

    if payment_obj:
        stripe_product = form_stripe_product(payment_obj)
        stripe_price = form_stripe_price(amount, stripe_product)
        line_items = form_line_items(stripe_price)

    return stripe.checkout.Session.create(
        success_url=success_url,
        line_items=[
            line_items,
        ],
        mode='payment',
    )


def get_id_of_payment_obj(
        paid_lesson_id: int or None,
        paid_course_id: int or None) -> Course or Lesson or None:
    if paid_course_id:
        return Course.objects.get(pk=paid_course_id)

    return Lesson.objects.get(pk=paid_lesson_id)


def form_stripe_product(
        payment_obj: Course or Lesson) -> stripe.Product:
    return stripe.Product.create(name=payment_obj.name)


def form_stripe_price(
        amount: int,
        stripe_product: stripe.Product) -> stripe.Price:
    return stripe.Price.create(
        unit_amount=amount * 100,
        currency='rub',
        product=stripe_product.stripe_id,
    )


def form_line_items(
        stripe_price: stripe.Price,
        quantity: int = 1) -> dict:
    return {
        'price': stripe_price.stripe_id,
        'quantity': quantity,
    }


def save_serializer(
        self,
        session: stripe.checkout.Session,
        serializer: serializers) -> None:
    serializer.save(
        stripe_payment_id=session.get('id'),
        stripe_payment_url=session.get('url'),
        status=session.get('status'),
        user=self.request.user,
        method=Payment.TRANSFER,
    )


def get_payment_info(stripe_payment_id: str) -> None:
    stripe.api_key = STRIPE_TOKEN
    return stripe.checkout.Session.retrieve(
        stripe_payment_id,
    )
