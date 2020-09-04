Models
======

A *Product* is composed of *Materials*.

Materials come in packages, for example 18 metal rings, or 1 meter of fabric.

The creator buys materials, makes products, and sells them.

### Product
 
A completed product ready to sell.

Fields:

- name
- photos
- time cost: in hours, to make the product
- target price
- stock: number of items available to sell

Relations:

- materials: list, with units used
- sales: list of past sales, dates and prices

Computed fields:

- material cost
- total sales

Actions:

- Start making: remove the required units from Materials
- Done making: update stock: +1
- Sold (for target price): update stock: -1; record the Sale
- Clone: make a clone of this product to customize

### Material

Material used to make products.

- name
- photos
- price per package
- units per package: can be a discrete value like 18 rings
    can be a "continuous" value like 100cm
    can be partly consumed
- stock: number of units available
- link to buy

Relations:

- products that require the material
- purchases of the material

Actions:

- Buy one package: update stock: +1; record Purchase

### `ProductMaterial`

The link between products and the materials they require.

Fields:

- product
- material
- units

### `ProductSale`

The link between products and sales.

Fields:

- product
- price
- date

### `MaterialPurchase`

The link between materials and purchases.

Fields:

- material
- price
- date
