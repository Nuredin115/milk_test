# -*- coding: utf-8 -*-
# Copyright (C) 2023 Konos and MercadoPago S.A.
# Licensed under the GPL-3.0 License or later.

{
    "name": "POS Telebirr",

    "summary": """
        Integrate your POS with a Redelcom payment terminal
    """,

    "author": "Konos Soluciones & Servicios",
    "website": "https://www.konos.cl",

    "category": "Sales/Point of Sale",
    "version": "17.0.0.1",

    "depends": [
        "point_of_sale","base"
    ],
# "qweb":[
#         "views/PaymentScreenPaymentLines.xml",

# ],

    "data": [
        "security/ir.model.access.csv",
        "wizard/payment_status.xml",
        "views/pos_payment_method_views.xml",

    ],
    "assets": {
        "point_of_sale._assets_pos": [
            "/pos_redelcom1/static/**/*",
            "/pos_redelcom1/static/src/**/*",
            'pos_redelcom1/static/src/app/*',
            "pos_redelcom1/static/src/overrides/components/payment_screen/payment_screen_payment_lines/test"

            # "/pos_redelcom1/views/pos_payment_method_views.xml"
        ],
    },

    "installable": True,
    "license": "GPL-3",
}
