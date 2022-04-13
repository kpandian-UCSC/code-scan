const axios = require("axios")
//const b64 = require("base64")

axios.get("https://api.github.com/repos/kpandian-ucsc/dummy-ci/contents/.github/workflows/tests.yml?ref=5c787395943d2719d4e821404be1a49c76fa1358").then((data) => {
    let buff = new Buffer(data.data.content, 'base64');
    let text = buff.toString('ascii');
    console.log(text)
})

