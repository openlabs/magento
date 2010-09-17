#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
    magento.catalog

    Product Catalog API for magento

    :copyright: (c) 2010 by Sharoon Thomas.
    :license: GPLv3, see LICENSE for more details
'''

from .api import API

class Category(API):
    """
    Product Category API to connect to magento
    """
    __slots__ = ( )

    def currentStore(self, store_view=None):
        """
        Set/Get current store view

        :param store_view: Store view ID or Code
        :return: int
        """
        if store_view is None:
            return int(self.call('catalog_category.currentStore', []))
        else:
            return int(self.call('catalog_category.currentStore', [store_view]))

    def tree(self, parent_id=None, store_view=None):
        """
        Retrieve hierarchical tree of categories.

        :param parent_id: Integer ID of parent category (optional)
        :param store_view: Store View (optional)
        :return: dictionary of values
        """
        return self.call('catalog_category.tree', [parent_id, store_view])

    def level(self, website=None, store_view=None, parent_category=None):
        """
        Retrieve one level of categories by website/store view/parent category
        
        :param website: Website code or ID
        :param store_view: storeview code or ID
        :param parent_category: Parent Category ID
        :return: Dictionary
        """
        return self.call('catalog_category.level', [
                                                    website, 
                                                    store_view, 
                                                    parent_category,
                                                    ]
        )

    def info(self, category_id, store_view=None, attributes=None):
        """
        Retrieve Category details

        :param category_id: ID of category to retrieve
        :param store_view: Store view ID or code
        :param attributes: Return the fields specified
        :return: Dictionary of data
        """
        return self.call('catalog_category.info', [
                                                    category_id,
                                                    store_view,
                                                    attributes,
                                                    ]
        )

    def create(self, parent_id, data, store_view=None):
        """
        Create new category and return its ID

        :param parent_id: ID of parent
        :param data: Data for category
        :param store_view: Store view ID or Code
        :return: Integer ID
        """
        return int(self.call('catalog_category.create', [
                                                         parent_id,
                                                         data,
                                                         store_view,
                                                         ])
        )

    def update(self, category_id, data, store_view=None):
        """
        Update Category

        :param category_id: ID of category
        :param data: Category Data
        :param store_view: Store view ID or code
        :return: Boolean
        """
        return bool(self.call('catalog_category.update', [
                                                          category_id,
                                                          data,
                                                          store_view,
                                                          ])
        )

    def move(self, category_id, parent_id, after_id=None):
        """
        Move category in tree

        :param category_id: ID of category to move
        :param parent_id: New parent of the category
        :param after_id: Category ID after what position it will be moved
        :return: Boolean 
        """
        return bool(self.call('catalog_category.move', [
                                                        category_id,
                                                        parent_id,
                                                        after_id,
                                                        ])
        )

    def delete(self, category_id):
        """
        Delete category

        :param category_id: ID of category
        :return: Boolean
        """
        return bool(self.call('catalog_category.delete', [
                                                          category_id
                                                            ])
        )

    def assignedproducts(self, category_id, store):
        """
        Retrieve list of assigned products

        :param category_id: Category ID
        :param store: Store ID or Code

        :return: Dictionary
        """
        return self.call('catalog_category.assignedProducts', [
                                                                category_id,
                                                                store,
                                                                ]
        )
    assigned_products = assignedproducts

    def assignproduct(self, category_id, product, position=None):
        """
        Assign product to a category
        
        :param category_id: ID of a category
        :param product: ID or Code of the product
        :param position: Position of product in category

        :return: boolean
        """
        return bool(self.call('catalog_category.assignProduct', [
                                                                 category_id,
                                                                 product,
                                                                 position,
                                                                ])
        )
    assign_product = assignproduct

    def updateproduct(self, category_id, product_id, position=None):
        """
        Update assigned product
        :param category_id: ID of a category
        :param product: ID or Code of the product
        :param position: Position of product in category

        :return: boolean
        """
        return bool(self.call('catalog_category.updateProduct', [
                                                                 category_id,
                                                                 product,
                                                                 position,
                                                                ])
        )
    
    update_product = updateproduct

    def removeproduct(self, category_id, product):
        """
        Remove product from category
        :param category_id: ID of a category
        :param product: ID or Code of the product

        :return: boolean
        """
        return bool(self.call('catalog_category.removeProduct', [
                                                                 category_id,
                                                                 product,
                                                                 ])
        )
    remove_product = removeproduct
        

class CategoryAttribute(API):
    """
    Product Category Attribute API to connect to magento
    Allows to get attributes and options for category.
    """
    __slots__ = ( )

    def currentStore(self, store_view=None):
        """
        Set/Get current store view

        :param store_view: Store view ID or Code
        :return: int
        """
        if store_view is None:
            return int(self.call('catalog_category_attribute.currentStore', []))
        else:
            return int(self.call('catalog_category_attribute.currentStore', 
                                [store_view])
            )

    def list(self):
        """
        Retrieve Category attrbutes
        """
        return self.call('category_attribute.list', [])

    def options(self, attribute_id, store_view=None):
        """
        Retrieve attribute options

        :param attribute_id: ID of the attribute whose options are reqd
        :param store_view: ID or Code of the store view

        :return: list of dictionary
        """
        return self.call('category_attribute.options', [attribute_id, 
                                                        store_view])
    

class Product(API):
    """
    Product API for magento
    """
    __slots__ = ( )

    def currentStore(self, store_view=None):
        """
        Set/Get current store view

        :param store_view: Store view ID or Code
        :return: int
        """
        if store_view is None:
            return int(self.call('catalog_product.currentStore', []))
        else:
            return int(self.call('catalog_product.currentStore', [store_view])
            )
    
    def list(self, filters=None, store_view=None):
        """
        Retrieve product list by filters
        
        :param filters: Dictionary of filters.
            Format :
                `{<attribute>:{<operator>:<value>}}`
            Example :
                `{'firstname':{'ilike':'sharoon'}}` 
        :store_view: Code or ID of store view
        :return: `list` of `dict`               
        """
        return self.call('catalog_product.list', [filters, store_view])

    def info(self, product, store_view=None, attributes=None):
        """
        Retrieve product data

        :param product: ID or SKU of product
        :param store_view: ID or Code of store view
        :param attributes: List of fields required
        :return: `dict` of values
        """
        return self.call('catalog_product.info', [product, 
                                                  store_view, 
                                                  attributes]
        )

    def create(self, product_type, attribute_set_id, sku, data):
        """
        Create Product and return ID

        :param product_type: String type of product
        :param attribute_set_id: ID of attribute set
        :param sku: SKU of the product
        :param data: Dictionary of data
        :return: INT id of product created
        """
        return int(self.call('catalog_product.create', [
                                                        product_type,
                                                        attribute_set_id,
                                                        sku,
                                                        data,
                                                        ])
        )

    def update(self, product, data, store_view=None):
        """
        Update product Information

        :param product: ID or SKU of product
        :param data: Dictionary of attributes to update
        :param store_view: ID or Code of store view

        :return: Boolean 
        """
        return bool(self.call('catalog_product.update', [
                                                         product,
                                                         data,
                                                         store_view,
                                                        ])
        )

    def setSpecialPrice(self, product, special_price=None, 
                        from_date=None, to_date=None, store_view=None):
        """
        Update product's special price

        :param product: ID or SKU of product
        :param special_price: Special Price
        :param from_date: From date
        :param to_date: To Date
        :param store_view: ID or Code of Store View

        :return: Boolean
        """
        return bool(self.call('catalog_product.setSpecialPrice', [
                                                                  product,
                                                                  special_price,
                                                                  from_date,
                                                                  to_date,
                                                                  store_view
                                                                    ])
        )

    def getSpecialPrice(self, product, store_view=None):
        """
        Get product special price data
        
        :param product: ID or SKU of product
        :param store_view: ID or Code of Store view

        :return: Dictionary
        """
        return self.call('catalog_product.getSpecialPrice', [
                                                             product,
                                                             store_view,
                                                            ]
        )

    def delete(self, product):
        """
        Delete a product

        :param product: ID or SKU of product
        :return: Boolean
        """
        return bool(self.call('catalog_product.delete', [product])
        )


class ProductAttribute(API):
    """
    Product Attribute API
    """
    __slots__ = ( )


class ProductAttributeSet(API):
    """
    Product Attribute Set API
    """
    __slots__ = ( )


class ProductTypes(API):
    """
    Product Types API
    """
    __slots__ = ( )


class ProductImages(API):
    """
    Product Images API
    """
    __slots__ = ( )


class ProductTierPrice(API):
    """
    Product Tier Price API
    """
    __slots__ = ( )


class ProductLinks(API):
    """
    Product links API (related, cross sells, up sells, grouped)
    """
    __slots__ = ( )


class Inventory(API):
    """
    Allows to update stock attributes (status, quantity)
    """
    __slots__ = ( )

