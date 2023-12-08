{
    "name": "revision module",
    "author": "Paana Software LLC",
    "website": "paana.com",
    "depends": ["base", "web", "website"],
    "data": [
        "security/ir.model.access.csv",
        "views/index.xml",
        "views/menu.xml",
        "views/website_menu.xml",
        "views/user_form.xml",
    ],
    "assets": {
        "web.assets_frontend": [
            "revision_module/static/src/css/index.css",
            "revision_module/static/src/js/index.js"
        ],
        # "web_assets_backend": [
        #     "revision_module/static/src/css/index.css"
        #     "revision_module/static/src/js/index.js"
        # ],
    },
}
