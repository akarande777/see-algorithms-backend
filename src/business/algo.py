from ..database.models import Category
from ..utils import *


class Algo:
    def __init__(self, context):
        self.session = context['session']

    def get_algorithms(self):
        try:
            categories = self.session.query(Category).all()
            return resolve(categories)
        except Exception:
            return reject("Internal server error")
