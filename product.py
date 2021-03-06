# This file is part of purchase_product_supplier module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta

__all__ = ['ProductSupplier']


class ProductSupplier:
    __metaclass__ = PoolMeta
    __name__ = 'purchase.product_supplier'
    product_code = fields.Function(
        fields.Char('Product Code'), 'get_product_code',
        searcher='search_product_code_field')

    def get_product_code(self, name):
        if not self.product:
            return None
        if self.product.code:
            return self.product.code
        else:
            return None

    @classmethod
    def search_product_code_field(cls, name, clause):
        return [('product.products.code',) + tuple(clause[1:])]

    @classmethod
    def search_rec_name(cls, name, clause):
        domain = super(ProductSupplier, cls).search_rec_name(name, clause)
        if clause[1].startswith('!') or clause[1].startswith('not '):
            bool_op = 'AND'
        else:
            bool_op = 'OR'
        return [bool_op,
            domain,
            ('product.products.code',) + tuple(clause[1:])
            ]
