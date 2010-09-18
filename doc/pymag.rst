Magento API
***********

Magento Module
--------------

.. automodule:: magento

API
---

.. automodule:: api

   .. autoclass:: API

      .. automethod:: __init__
      .. automethod:: connect
      .. automethod:: __enter__
      .. automethod:: __exit__
      .. automethod:: call
      .. automethod:: multiCall

Catalog
-------

.. automodule:: catalog

   .. autoclass:: Category

      .. automethod:: currentStore
      .. automethod:: tree
      .. automethod:: level
      .. automethod:: info
      .. automethod:: create
      .. automethod:: update
      .. automethod:: move
      .. automethod:: delete
      .. automethod:: assignedproducts
      .. automethod:: assignproduct
      .. automethod:: updateproduct
      .. automethod:: removeproduct


   .. autoclass:: CategoryAttribute

      .. automethod:: currentStore
      .. automethod:: options
      .. automethod:: list



   .. autoclass:: Product

      .. automethod:: currentStore
      .. automethod:: list
      .. automethod:: info
      .. automethod:: create
      .. automethod:: update
      .. automethod:: setSpecialPrice
      .. automethod:: getSpecialPrice
      .. automethod:: delete

   .. autoclass:: ProductAttribute

   .. autoclass:: ProductAttributeSet

   .. autoclass:: ProductTypes

   .. autoclass:: ProductImages

   .. autoclass:: ProductTierPrice

   .. autoclass:: ProductLinks

   .. autoclass:: Inventory

Customer
--------

.. automodule:: customer

   .. autoclass:: Customer

      .. automethod:: list
      .. automethod:: create
      .. automethod:: info
      .. automethod:: update
      .. automethod:: delete

   .. autoclass:: CustomerGroup

      .. automethod:: list

   .. autoclass:: CustomerAddress

      .. automethod:: list
      .. automethod:: create
      .. automethod:: info
      .. automethod:: update
      .. automethod:: delete

Directory
---------

.. automodule:: directory

   .. autoclass:: Country

      .. automethod:: list

   .. autoclass:: Region

      .. automethod:: list

Utils
-----

.. automodule:: utils

   .. autofunction:: expand_url

.. automodule:: custom_api
