odoo.define(
    'require'
    ,
    function () {
        'use strict';
        console.log("shown")

        var btnTest = document.querySelector("#showToastBtn")
        btnTest.addEventListener("click", (e) => {
            alert(e.type) 
        })
    },

);