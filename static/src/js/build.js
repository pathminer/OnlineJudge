({
	// RequireJS 通过一个相对的路径 baseUrl来加载所有代码。baseUrl通常被设置成data-main属性指定脚本的同级目录。
	baseUrl: "js/",
	// 第三方脚本模块的别名,jquery比libs/jquery-1.11.1.min.js简洁明了；
    paths: {
        //百度webuploader
        webuploader: "lib/webuploader/webuploader",

        jquery: "lib/jquery/jquery",
        avalon: "lib/avalon/avalon",
        editor: "utils/editor",
        uploader: "utils/uploader",
        validation: "utils/validation",
        code_mirror: "utils/code_mirror",
        login: "app/account/login",
        oj: "app/oj",
        "bs_alert": "utils/bs_alert",
        submit_code: "app/problem/submit_code",

        //formValidation 不要在代码中单独使用，而是使用和修改utils/validation
        base: "lib/formValidation/base",
        helper: "lib/formValidation/helper",
        "language/zh_CN": "lib/formValidation/language/zh_CN",
        "framework/bootstrap": "lib/formValidation/framework/bootstrap",
        "validator/notEmpty": "lib/formValidation/validator/notEmpty",
        "validator/stringLength": "lib/formValidation/validator/stringLength",
        "validator/date": "lib/formValidation/validator/date",
        "validator/integer": "lib/formValidation/validator/integer",
        "validator/between": "lib/formValidation/validator/between",

        //富文本编辑器 不要直接使用，而是使用上面的editor
        simditor: "lib/simditor/simditor",
        "simple-module": "lib/simditor/module",
        "simple-hotkeys": "lib/simditor/hotkeys",
        "simple-uploader": "lib/simditor/uploader",

        //code mirroe 代码编辑器
        _code_mirror: "lib/codeMirror/codemirror",
        code_mirror_clang: "lib/codeMirror/language/clike",

        //bootstrap
        bootstrap: "lib/bootstrap/bootstrap"

    },
    shim: {
        "bootstrap": {"deps": ['jquery']}
    },
    findNestedDependencies: true,
    appDir: "../",
    dir: "../../release/",
    modules: [
        {
            name: "oj"
        }
    ]
})