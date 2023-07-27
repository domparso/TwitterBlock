/*
*
 */


function packMsgReq(type, data) {
    return {
        uuid: function () {
            return 'generate-uuid-4you-seem-professional'.replace(
                /[genratuidyosmpfl]/g, function (c) {
                    const r = Math.random() * 16 | 0,
                        v = c === 'x' ? r : (r & 0x3 | 0x8)
                    return v.toString(16)
                })
        }(),
        type: type,
        data: data,
        timestamp: Date.now()
    }
}

const client = {
    request: function (options) {
        return new Promise((resolve, reject) => {
            // Uncaught (in promise) Error: Extension context invalidated
            if(chrome.runtime.id == undefined) return

            chrome.runtime.sendMessage(packMsgReq('FetchRequest', options),
                (response) => {
                    if (response.state) {
                        resolve(response.data)
                    } else {
                        reject(response.data)
                    }
                }
            )
        })
    },
    get: function (options) {
        return new Promise((resolve, reject) => {
            // Uncaught (in promise) Error: Extension context invalidated
            if(chrome.runtime.id == undefined) return

            chrome.runtime.sendMessage(packMsgReq('FetchGet', options),
                (response) => {
                    if (response.state) {
                        resolve(response.data)
                    } else {
                        reject(response.data)
                    }
                }
            )
        })
    },
    post: function (options) {
        return new Promise((resolve, reject) => {
            // Uncaught (in promise) Error: Extension context invalidated
            if(chrome.runtime.id == undefined) return

            chrome.runtime.sendMessage(packMsgReq('FetchPost', options),
                (response) => {
                    if (response.state) {
                        resolve(response.data)
                    } else {
                        reject(response.data)
                    }
                }
            )
        })
    },
    postForm: function (options) {
        return new Promise((resolve, reject) => {
            // Uncaught (in promise) Error: Extension context invalidated
            if(chrome.runtime.id == undefined) return

            chrome.runtime.sendMessage(packMsgReq('FetchPostForm', options),
                (response) => {
                    if (response.state) {
                        resolve(response.data)
                    } else {
                        reject(response.data)
                    }
                }
            )
        })
    }
}


function myTrim (x) {
    return x.replace(/^\s+|\s+$/gm, '')
}

function isEmptyStr (str) {
    if (str != null && myTrim(str).length > 0) {
        return false
    }
    return true
}

// function getCookies (name) {
//     var cookiesMap
//     $(() => {
//         chrome.tabs.query(
//             {'active': true, lastFocusedWindow: true},
//             (tabs) => {
//                 const url = tabs[0].url
//                 chrome.cookies.getAll({
//                     domain: url.host
//                 }, (cookies) => {
//                     cookiesMap = cookies
//                 })
//         })
//     })
//     cookiesMap.forEach((item) => {
//         if (item.name == name) {
//             return item.value
//         }
//     })
//     return ''
// }

function getCookie(key) {
    const cookies = document.cookie.split(";")
    for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim().split("=")
        if (cookie[0] === key) {
            return cookie[1]
        }
    }
    return null
}