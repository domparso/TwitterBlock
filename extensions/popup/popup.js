/*
*
 */

$(document).ready(() => {
    // 获取本地数据
    $(() => {
        chrome.storage.sync.get(
            ['custom_block','custom_unblock'],
            (budget) => {
                $('#custom-block-list').val(budget.custom_block)
                $('#custom-unblock-list').val(budget.custom_unblock)
            })
    })

    // 读取cookie
    var cookiesMap
    $(() => {
        chrome.tabs.query({'active': true, lastFocusedWindow: true},
            (tabs) => {
            const url = tabs[0].url
            chrome.cookies.getAll({
                domain: url.host
            }, (cookies) => {
                cookiesMap = cookies
                // $('#custom-block-list').val(cookies.map(c => c.name+"="+c.value).join(';'))
            })
        })
    })

    // add block
    $('#addBlock').click(() => {
        if ($('#input-block').val() == '') {
            return
        }

        var tmp = $('#custom-block-list').val()
        if (tmp === '') {
            tmp = $('#input-block').val()
        } else {
            tmp = $('#input-block').val() + '\n' + tmp
        }
        $('#custom-block-list').val(tmp)
        $('#input-block').val('')
    })
    // add unblock
    $('#addUnblock').click(() => {
        if ($('#input-unblock').val() == '') {
            return
        }

        var tmp = $('#custom-unblock-list').val()

        if (tmp === '') {
            tmp = $('#input-unblock').val()
        } else {
            tmp = $('#input-unblock').val() + '\n' + tmp
        }
        $('#custom-unblock-list').val(tmp)
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
    // coin
    $('#coin').click(() => {
        color = $("#coin").css("background-color")
        if (color == "rgb(255, 255, 255)") {
            $('#coin').css("background-color","red")
        }
        else {
            $('#coin').css("background-color","white")
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
        $('#saveHint').html("正在生效...")

        var blockList = []
        var customBlockList = $('#custom-block-list').val()
        var customUnblockList = $('#custom-unblock-list').val()
        chrome.storage.sync.set({
            'custom_block': customBlockList,
            'custom_unblock': customUnblockList
        })

        var pornList = '';
        color = $("#porn").css("background-color")
        if (color == "rgb(255, 0, 0)") {
            client.get({
                url: "https://raw.githubusercontent.com/domparso/TwitterBlock/master/blocklist/porn.txt"
            }).then((data) => {
                pornList = data.body
                if (! isEmptyStr(pornList)) {
                    pornList = pornList.split('\n')
                    blockList = blockList.concat(pornList)
                }
            })
        }

        var coinList = ''
        color = $("#coin").css("background-color")
        if (color == "rgb(255, 0, 0)") {
            client.get({
                url: "https://raw.githubusercontent.com/domparso/TwitterBlock/master/blocklist/coin.txt"
            }).then((data) => {
                coinList = data.body
                if (coinList !== '') {
                    coinList = coinList.split('\n')
                    blockList = blockList.concat(coinList)
                }
            })
        }


        var otherList = ''
        color = $("#other").css("background-color")
        if (color == "rgb(255, 0, 0)") {
            client.get({
                url: "https://raw.githubusercontent.com/domparso/TwitterBlock/master/blocklist/other.txt"
            }).then((data) => {
                otherList = data.body
                if (otherList != '') {
                    otherList = otherList.split('\n')
                    blockList = blockList.concat(otherList)
                }
            })
        }

        if (blockList.length == 0) {
            $('#saveHint').html("已生效...")
        } else {
            setTimeout(() => {
                let ct0 = ''
                let lang = ''
                cookiesMap.forEach((item) => {
                    if (item.name == 'ct0') {
                        ct0 = item.value
                    } else if (item.name == 'lang') {
                        lang = item.value
                    }
                })
                // client.postForm({
                //     url: "https://twitter.com/i/api/1.1/blocks/create.json",
                //     data: "user_id=2986012495",
                //
                // }).then((data) => {
                //     // $('#custom-unblock-list').val($('#custom-unblock-list').val() + '\n' + data.body)
                // })

                Array.from(new Set(blockList)).forEach((item) => {
                    setTimeout(() => {
                        tmp = item.split(',')
                        userId = tmp[0]
                        client.postForm({
                            url: "https://twitter.com/i/api/1.1/blocks/create.json?",
                            data: "user_id=" + userId,
                            headers: {
                                "Authorization": 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
                                "X-Csrf-Token": ct0,
                                "X-Twitter-Auth-Type": "OAuth2Session",
                                "X-Twitter-Client-Language": lang
                            }
                        })
                    }, 2000)
                })

                $('#saveHint').html("已生效...")
            }, 6000)
        }

        setTimeout(() => {
            $('#saveHint').html("")
        }, 10000)
    })

})
