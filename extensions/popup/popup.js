/*
*
 */


const SETINTERVAL = 5000

var blockList = []
var unBlockList = []
// 读取cookie
var lang, ct0, headers, cookiesMap


function getUserInfo(screenName, callback) {
    // get userid
    twurl = "https://twitter.com/i/api/graphql/oUZZZ8Oddwxs8Cd3iW3UEA/UserByScreenName?variables=%7B%22screen_name%22%3A%22" + screenName + "%22%2C%22withSafetyModeUserFields%22%3Atrue%7D&features=%7B%22hidden_profile_likes_enabled%22%3Afalse%2C%22responsive_web_graphql_exclude_directive_enabled%22%3Atrue%2C%22verified_phone_label_enabled%22%3Afalse%2C%22subscriptions_verification_info_verified_since_enabled%22%3Atrue%2C%22highlights_tweets_tab_ui_enabled%22%3Atrue%2C%22creator_subscriptions_tweet_preview_api_enabled%22%3Atrue%2C%22responsive_web_graphql_skip_user_profile_image_extensions_enabled%22%3Afalse%2C%22responsive_web_graphql_timeline_navigation_enabled%22%3Atrue%7D"
    client.get({
        url: twurl,
        headers: headers
    }).then((data) => {
        callback(data)
    })
}

function getList(filename, callback) {
    client.get({
        url: "https://raw.githubusercontent.com/domparso/TwitterBlock/master/blocklist/" + filename
    }).then((data) => {
        callback(data)
    })
}


// data ['other', userId, state]
function reportUserState(data) {
    client.post({
        url: "https://example.com/api/v1/twitterblocker/set",
        data: data
    })
}

function delayLoopUsingSetTimeout(max, callback) {
    index = 0

    function loop() {
        if (index < max) {
            callback(index)
            index++
            setTimeout(loop, SETINTERVAL)
        } else {
            console.log("finish")
            $('#saveHint').html(i18n[lang]["hint"][2])
        }
    }

    loop()
}

function recursion(index, max, callback) {
    index = 0
    if (index < max) {
        callback(index)
        index++
        setTimeout(() => {
            recursion(index, max, callback)
        }, SETINTERVAL)
    }
}

function blockUser(userId) {
    client.postForm({
        url: "https://twitter.com/i/api/1.1/blocks/create.json?",
        data: "user_id=" + userId,
        headers: headers
    }).then((data) => {
        result = JSON.parse(data.body)
        if (result.errors) {
            reportUserState(["banned", userId])
        }

    })
}

function unBlockUser(userId) {
    client.postForm({
        url: "https://twitter.com/i/api/1.1/blocks/destroy.json?",
        data: "user_id=" + userId,
        headers: headers
    })
}

$(document).ready(() => {
    // 读取cookie
    chrome.tabs.query(
        {'active': true, lastFocusedWindow: true},
        (tabs) => {
            const url = tabs[0].url
            chrome.cookies.getAll({
                domain: url.host
            }, (cookies) => {
                cookiesMap = cookies
                // $('#custom-unblock-list').val(cookies.map(c => c.name+"="+c.value).join(';'))
            })
        })

    setTimeout(() => {
        cookiesMap.forEach((item) => {
            if (item.name == 'lang') {
                lang = item.value
            } else if (item.name == 'ct0') {
                ct0 = item.value
            }
        })

        if (isEmptyStr(lang) || isEmptyStr(ct0)) {
            $('#saveHint').html(i18n[lang]["hint"][0])
            return
        }

        headers = {
            "Authorization": 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
            "X-Csrf-Token": ct0,
            "X-Twitter-Auth-Type": "OAuth2Session",
            "X-Twitter-Client-Language": lang
        }
        // $('#custom-block-list').val(JSON.stringify(headers))

        $('title').text(i18n[lang]["title"])
        $('#options').text(i18n[lang]["options"])
        $('#porn').text(i18n[lang]["porn"])
        $('#other').text(i18n[lang]["other"])
        $('#custom-block-options').text(i18n[lang]["custom-block-options"])
        $('#addBlock').text(i18n[lang]["addBlock"])
        $('#cleanBlock').text(i18n[lang]["cleanBlock"])

        $('#custom-unblock-options').text(i18n[lang]["custom-unblock-options"])
        $('#addUnblock').text(i18n[lang]["addUnblock"])
        $('#cleanUnblock').text(i18n[lang]["cleanUnblock"])
        $('#save').text(i18n[lang]["save"])

    }, 500)

    // 获取本地数据
    $(() => {
        chrome.storage.sync.get(
            ['custom_block','custom_unblock'],
            (budget) => {
                $('#custom-block-list').val(budget.custom_block)
                $('#custom-unblock-list').val(budget.custom_unblock)
            })
    })

    // add block
    $('#addBlock').click(() => {
        if ($('#input-block').val() == '') {
            return
        }

        var tmp = $('#custom-block-list').val()
        name = $('#input-block').val()
        getUserInfo(name, (data) => {
            try {
                result = JSON.parse(data.body)
            } catch (e) {
                $('#saveHint').html(e)
                return
            }
            userId = result.data.user.result.rest_id
            screenName = result.data.user.result.legacy.screen_name
            name = result.data.user.result.legacy.name
            if (tmp === '') {
                tmp = [userId, screenName, name].join(',')
            } else {
                tmp = [userId, screenName, name].join(',') + '\n' + tmp
            }

            $('#custom-block-list').val(tmp)
        })

        $('#input-block').val('')
    })
    // add unblock
    $('#addUnblock').click(() => {
        if ($('#input-unblock').val() == '') {
            return
        }

        var tmp = $('#custom-unblock-list').val()
        name = $('#input-unblock').val()
        getUserInfo(name, (data) => {
            try {
                result = JSON.parse(data.body)
            } catch (e) {
                $('#saveHint').html(e)
                return
            }
            userId = result.data.user.result.rest_id
            screenName = result.data.user.result.legacy.screen_name
            name = result.data.user.result.legacy.name
            if (tmp === '') {
                tmp = [userId, screenName, name].join(',')
            } else {
                tmp = [userId, screenName, name].join(',') + '\n' + tmp
            }

            $('#custom-unblock-list').val(tmp)
        })
        $('#input-unblock').val('')
    })

    // clean block
    $('#cleanBlock').click(() => {
        $('#custom-block-list').val('')
    })
    // clean unblock
    $('#cleanUnblock').click(() => {
        $('#custom-unblock-list').val('')
    })

    // porn
    $('#porn').click(() => {
        color = $("#porn").css("background-color")
        if (color == "rgb(255, 255, 255)") {
            $('#porn').css("background-color","red")
        }
        else {
            $('#porn').css("background-color","white")
        }
    })
    // other
    $('#other').click(() => {
        color = $("#other").css("background-color")
        if (color == "rgb(255, 255, 255)") {
            $('#other').css("background-color","red")
        }
        else {
            $('#other').css("background-color","white")
        }
    })

    // 保存数据
    $('#save').click(() => {
        // $('#saveHint').html("正在生效...")
        $('#saveHint').html(i18n[lang]["hint"][1])

        var customBlockList = $('#custom-block-list').val()
        var customUnblockList = $('#custom-unblock-list').val()
        chrome.storage.sync.set({
            'custom_block': customBlockList,
            'custom_unblock': customUnblockList
        })

        color = $("#porn").css("background-color")
        if (color == "rgb(255, 0, 0)") {
            getList("porn.txt", (result) => {
                data = result.body
                if (data != '') {
                    data.split('\n').forEach((item) => {
                        if (item != '') {
                            blockList.push(item.split(',')[0])
                        }
                    })
                }
                $('#custom-block-list').val(blockList.join('\n'))
            })
        }

        color = $("#other").css("background-color")
        if (color == "rgb(255, 0, 0)") {
            getList("other.txt", (result) => {
                data = result.body
                if (data != '') {
                    data.split('\n').forEach((item) => {
                        if (item != '' && item.split(',')[0] != '') {
                            blockList.push(item.split(',')[0])
                        }
                    })
                }
            })
        }

        setTimeout(() => {
            customBlockList.split('\n').forEach((item) => {
                if (item != '') {
                    blockList.push(item.split(',')[0])
                }
            })

            if (blockList.length == 0) {
                // $('#saveHint').html("已生效...")
                $('#saveHint').html(i18n[lang]["hint"][2] + '  ' + blockList.length)
            } else {
                // client.postForm({
                //     url: "https://twitter.com/i/api/1.1/blocks/create.json",
                //     data: "user_id=2986012495",
                //
                // }).then((data) => {
                //     // $('#custom-unblock-list').val($('#custom-unblock-list').val() + '\n' + data.body)
                // })
                blockList = Array.from(new Set(blockList))
                delayLoopUsingSetTimeout(blockList.length, (index) => {
                    if (blockList[index] != '' && blockList[index] != undefined && blockList[index] != '\n') {
                        blockUser(blockList[index])
                        // $('#custom-unblock-list').val($('#custom-unblock-list').val() + '\n' + blockList[index])
                    }
                })
            }
        }, 10000)

        setTimeout(() => {
            customUnblockList.split('\n').forEach((item) => {
                if (item != '') {
                    unBlockList.push(item.split(',')[0])
                }
            })

            if (unBlockList.length == 0) {
                $('#saveHint').html(i18n[lang]["hint"][2])
            } else {
                unBlockList = Array.from(new Set(unBlockList))
                delayLoopUsingSetTimeout(unBlockList.length, (index) => {
                    if (unBlockList[index] != '' && unBlockList[index] != undefined && unBlockList[index] != '\n') {
                        unBlockUser(unBlockList[index])
                    }
                })
            }
        }, 15000)

    })

})
