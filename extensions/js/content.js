/*
*
*/


var share_blockList

chrome.storage.sync.get(
    ['share_blockList'],
    (budget) => {
        porn_block = budget.share_blockList
    })

const lang = getCookie("lang")
const ct0 = getCookie("ct0")

var selfId = ''
const headers = {
    "Authorization": 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
    "X-Csrf-Token": ct0,
    "X-Twitter-Auth-Type": "OAuth2Session",
    "X-Twitter-Client-Language": lang
}

https://api.twitter.com/1/users/lookup.json?screen_name=somename
function getUserId(screen_name, callback) {
    url = "https://twitter.com/i/api/graphql/oUZZZ8Oddwxs8Cd3iW3UEA/UserByScreenName"
    client.post({
        url: "https://twitter.com/i/api/graphql/oUZZZ8Oddwxs8Cd3iW3UEA/UserByScreenName",
    }).then(callback())
}

// data ['other', userId, screenName, name]
function shareBlockTweet(blockData, callback) {
    client.post({
        url: "https://shadow.ssn571.boats/api/v1/twitterblocker/set",
        data: blockData,
    }).then((data) => {
        callback(data)
    })
}


function getPornButton() {
    let label = i18n[lang]["pornLabel"]

    return $(`<div role="menuitem" tabindex="0"
    class="css-1dbjc4n r-1loqt21 r-18u37iz r-1ny4l3l r-ymttw5 r-1f1sjgu r-o7ynqc r-6416eg r-13qz1uu" data-testid="mark">
      <div class="css-1dbjc4n r-1777fci r-j2kj52">
        <svg viewbox="0 0 24 24" aria-hidden="true"
        class="r-1nao33i r-4qtqp9 r-yyyyoo r-1q142lx r-1xvli5t r-dnmrzs r-bnwqim r-1plcrui r-lrvibr">
          <g>
            <path d="M12 3.75c-4.55 0-8.25 3.69-8.25 8.25 0 1.92.66 3.68 1.75 5.08L17.09 5.5C15.68 4.4 13.92 3.75 12 3.75zm6.5 3.17L6.92 18.5c1.4 1.1 3.16 1.75 5.08 1.75 4.56 0 8.25-3.69 8.25-8.25 0-1.92-.65-3.68-1.75-5.08zM1.75 12C1.75 6.34 6.34 1.75 12 1.75S22.25 6.34 22.25 12 17.66 22.25 12 22.25 1.75 17.66 1.75 12z">
            </path>
          </g>
        </svg>
      </div>
      <span style="color: orange">${label}</span>
      
 <!--     <div class="css-1dbjc4n r-16y2uox r-1wbh5a2">
        <div dir="ltr" class="css-901oao r-1nao33i r-1qd0xha r-a023e6 r-b88u0q r-rjixqe r-bcqeeo r-qvutc0">
          <span class="css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0">${label}</span>
        </div>
      </div> -->
    </div>`)
}

function getOtherButton() {
    let label = i18n[lang]["otherLabel"]

    return $(`<div role="menuitem" tabindex="0"
    class="css-1dbjc4n r-1loqt21 r-18u37iz r-1ny4l3l r-ymttw5 r-1f1sjgu r-o7ynqc r-6416eg r-13qz1uu" data-testid="mark">
      <div class="css-1dbjc4n r-1777fci r-j2kj52">
        <svg viewbox="0 0 24 24" aria-hidden="true"
        class="r-1nao33i r-4qtqp9 r-yyyyoo r-1q142lx r-1xvli5t r-dnmrzs r-bnwqim r-1plcrui r-lrvibr">
          <g>
            <path d="M12 3.75c-4.55 0-8.25 3.69-8.25 8.25 0 1.92.66 3.68 1.75 5.08L17.09 5.5C15.68 4.4 13.92 3.75 12 3.75zm6.5 3.17L6.92 18.5c1.4 1.1 3.16 1.75 5.08 1.75 4.56 0 8.25-3.69 8.25-8.25 0-1.92-.65-3.68-1.75-5.08zM1.75 12C1.75 6.34 6.34 1.75 12 1.75S22.25 6.34 22.25 12 17.66 22.25 12 22.25 1.75 17.66 1.75 12z">
            </path>
          </g>
        </svg>
      </div>
      <span style="color: orange">${label}</span>
      
 <!--      <div class="css-1dbjc4n r-16y2uox r-1wbh5a2">
        <div dir="ltr" class="css-901oao r-1nao33i r-1qd0xha r-a023e6 r-b88u0q r-rjixqe r-bcqeeo r-qvutc0" style="height: 20px;">
          <span class="css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0">${label}</span>
        </div>
      </div> -->
    </div>`)
}



function watchDOM (node, config) {
    moreLabel = i18n[lang]["more"]
    homeLabel = i18n[lang]["home"]

    const observer = new MutationObserver((mutations) => {
        mutations.forEach((mutation) => {
            // console.log("mutations")
        })

        // on 被重复调用
        more = $('[role="main"]').find('[aria-label*="' + homeLabel + '"]').find('[aria-label="' + moreLabel + '"]')
        more.off('click').on("click", () => {
            // console.log("click")
            setTimeout(() => {
                const menu = $('[role="menu"]')
                if (menu.length === 0) {
                    return
                } else {
                    const dropDown = menu.find('[data-testid="Dropdown"]')
                    height = dropDown.children().first().css("height")
                    markButton = getPornButton()
                    dropDown.append(markButton)
                    markButton.off('click').on("click", () => {
                        console.log("markButton click")
                        followButton = dropDown.find('[data-testid="block"]')
                        screen_name=followButton.text()
                        if (screen_name === '') {
                            console.log("screen_name is empty")
                            return
                        }

                        screen_name=screen_name.split('@')[1]

                        // get userid
                        twurl = "https://twitter.com/i/api/graphql/oUZZZ8Oddwxs8Cd3iW3UEA/UserByScreenName?variables=%7B%22screen_name%22%3A%22" + screen_name + "%22%2C%22withSafetyModeUserFields%22%3Atrue%7D&features=%7B%22hidden_profile_likes_enabled%22%3Afalse%2C%22responsive_web_graphql_exclude_directive_enabled%22%3Atrue%2C%22verified_phone_label_enabled%22%3Afalse%2C%22subscriptions_verification_info_verified_since_enabled%22%3Atrue%2C%22highlights_tweets_tab_ui_enabled%22%3Atrue%2C%22creator_subscriptions_tweet_preview_api_enabled%22%3Atrue%2C%22responsive_web_graphql_skip_user_profile_image_extensions_enabled%22%3Afalse%2C%22responsive_web_graphql_timeline_navigation_enabled%22%3Atrue%7D"
                        client.get({
                            url: twurl,
                            headers: headers
                        }).then((data) => {
                            try {
                                result = JSON.parse(data.body)
                            } catch (e) {
                                return
                            }
                            result = JSON.parse(data.body)
                            userId = result.data.user.result.rest_id
                            screenName = result.data.user.result.legacy.screen_name
                            name = result.data.user.result.legacy.name
                            console.log(userId, screenName, name)

                            // 发送block请求
                            client.postForm({
                                url: "https://twitter.com/i/api/1.1/blocks/create.json?",
                                data: "user_id=" + userId,
                                headers: headers
                            }).then((data) => {
                                console.log(data)
                                markButton.css("background-color", "red")
                            })

                            // share info
                            info = ['pron', userId, screenName, name]
                            shareBlockTweet(
                                info,
                                (data) => {
                                    if (data.body !== "1") {
                                        share_blockList = info.join(',') + '\n'
                                        chrome.storage.sync.set({
                                            'share_blockList': share_blockList
                                        })
                                    }
                                }

                            )

                            // send mark info
                            // client.post({
                            //     url: "https://twitter.com/i/api/1.1/dm/new2.json?ext=mediaColor%2CaltText%2CmediaStats%2ChighlightedLabel%2ChasNftAvatar%2CvoiceInfo%2CbirdwatchPivot%2CsuperFollowMetadata%2CunmentionInfo%2CeditControl&include_ext_alt_text=true&include_ext_limited_action_results=true&include_reply_count=1&tweet_mode=extended&include_ext_views=true&include_groups=true&include_inbox_timelines=true&include_ext_media_color=true&supports_reactions=true",
                            //     data: {
                            //         conversation_id: selfId + '-1678778319557496844',
                            //         recipient_ids: false,
                            //         request_id: 'web_ext_' + Date.now(),
                            //         text: ['porn', userId, screenName, name].join(','),
                            //         cards_platform: 'Web-12',
                            //         include_cards: 1,
                            //         include_quote_count: true,
                            //         dm_users: false
                            //     },
                            //     headers: hearders
                            // }).then((data) => {
                            //     console.log(data)
                            // })
                            //
                            // client.post({
                            //     url: "https://twitter.com/i/api/1.1/dm/new2.json?ext=mediaColor%2CaltText%2CmediaStats%2ChighlightedLabel%2ChasNftAvatar%2CvoiceInfo%2CbirdwatchPivot%2CsuperFollowMetadata%2CunmentionInfo%2CeditControl&include_ext_alt_text=true&include_ext_limited_action_results=true&include_reply_count=1&tweet_mode=extended&include_ext_views=true&include_groups=true&include_inbox_timelines=true&include_ext_media_color=true&supports_reactions=true",
                            //     data: {
                            //         conversation_id: selfId + '-1678778319557496844',
                            //         recipient_ids: false,
                            //         request_id: 'web_ext_' + Date.now(),
                            //         text: ['other', userId, screenName, name].join(','),
                            //         cards_platform: 'Web-12',
                            //         include_cards: 1,
                            //         include_quote_count: true,
                            //         dm_users: false
                            //     },
                            //     headers: headers
                            // }).then((data) => {
                            //     console.log(data)
                            // })

                        })
                    })

                    otherButton = getOtherButton()
                    dropDown.append(otherButton)
                    otherButton.off('click').on("click", () => {
                        console.log("otherButton click")
                        followButton = dropDown.find('[data-testid="block"]')
                        screen_name=followButton.text()
                        if (screen_name === '') {
                            console.log("screen_name is empty")
                            return
                        }

                        screen_name=screen_name.split('@')[1]

                        // get userid
                        twurl = "https://twitter.com/i/api/graphql/oUZZZ8Oddwxs8Cd3iW3UEA/UserByScreenName?variables=%7B%22screen_name%22%3A%22" + screen_name + "%22%2C%22withSafetyModeUserFields%22%3Atrue%7D&features=%7B%22hidden_profile_likes_enabled%22%3Afalse%2C%22responsive_web_graphql_exclude_directive_enabled%22%3Atrue%2C%22verified_phone_label_enabled%22%3Afalse%2C%22subscriptions_verification_info_verified_since_enabled%22%3Atrue%2C%22highlights_tweets_tab_ui_enabled%22%3Atrue%2C%22creator_subscriptions_tweet_preview_api_enabled%22%3Atrue%2C%22responsive_web_graphql_skip_user_profile_image_extensions_enabled%22%3Afalse%2C%22responsive_web_graphql_timeline_navigation_enabled%22%3Atrue%7D"
                        client.get({
                            url: twurl,
                            headers: headers
                        }).then((data) => {
                            try {
                                result = JSON.parse(data.body)
                            } catch (e) {
                                return
                            }
                            result = JSON.parse(data.body)
                            userId = result.data.user.result.rest_id
                            screenName = result.data.user.result.legacy.screen_name
                            name = result.data.user.result.legacy.name
                            console.log(userId, screenName, name)

                            // 发送block请求
                            client.postForm({
                                url: "https://twitter.com/i/api/1.1/blocks/create.json?",
                                data: "user_id=" + userId,
                                headers: headers
                            }).then((data) => {
                                // console.log(data)
                                otherButton.css("background-color", "red")
                            })

                            // share info
                            info = ['other', userId, screenName, name]
                            shareBlockTweet(
                                info,
                                (data) => {
                                    if (data.body !== "1") {
                                        share_blockList = info.join(',') + '\n'
                                        chrome.storage.sync.set({
                                            'share_blockList': share_blockList
                                        })
                                    }
                                }

                            )

                            // // send mark info
                            // client.post({
                            //     url: "https://twitter.com/i/api/1.1/dm/new2.json?ext=mediaColor%2CaltText%2CmediaStats%2ChighlightedLabel%2ChasNftAvatar%2CvoiceInfo%2CbirdwatchPivot%2CsuperFollowMetadata%2CunmentionInfo%2CeditControl&include_ext_alt_text=true&include_ext_limited_action_results=true&include_reply_count=1&tweet_mode=extended&include_ext_views=true&include_groups=true&include_inbox_timelines=true&include_ext_media_color=true&supports_reactions=true",
                            //     data: {
                            //         conversation_id: selfId + '-1678778319557496844',
                            //         recipient_ids: false,
                            //         request_id: 'web_ext_' + Date.now(),
                            //         text: [userId, screenName, name].join(','),
                            //         cards_platform: 'Web-12',
                            //         include_cards: 1,
                            //         include_quote_count: true,
                            //         dm_users: false
                            //     },
                            //     headers: headers
                            // }).then((data) => {
                            //     console.log(data)
                            // })
                            //
                            // client.post({
                            //     url: "https://twitter.com/i/api/1.1/dm/new2.json?ext=mediaColor%2CaltText%2CmediaStats%2ChighlightedLabel%2ChasNftAvatar%2CvoiceInfo%2CbirdwatchPivot%2CsuperFollowMetadata%2CunmentionInfo%2CeditControl&include_ext_alt_text=true&include_ext_limited_action_results=true&include_reply_count=1&tweet_mode=extended&include_ext_views=true&include_groups=true&include_inbox_timelines=true&include_ext_media_color=true&supports_reactions=true",
                            //     data: {
                            //         conversation_id: selfId + '-1678778319557496844',
                            //         recipient_ids: false,
                            //         request_id: 'web_ext_' + Date.now(),
                            //         text: ['other', userId, screenName, name].join(','),
                            //         cards_platform: 'Web-12',
                            //         include_cards: 1,
                            //         include_quote_count: true,
                            //         dm_users: false
                            //     },
                            //     headers: hearders
                            // }).then((data) => {
                            //     console.log(data)
                            // })

                        })
                    })
                }

            }, 200)
        })
    })

    observer.observe(node, config)
}

function main () {
    setTimeout(() => {
        profileLabel = i18n[lang]["profile"]
        AccountMenu = $('[aria-label="' + profileLabel + '"]')
        screen_name = AccountMenu.prop("href").split('/')
        screen_name = screen_name[screen_name.length-1]

        if (screen_name === '') {
            console.log("screen_name is null")
            return
        }
        twurl = "https://twitter.com/i/api/graphql/oUZZZ8Oddwxs8Cd3iW3UEA/UserByScreenName?variables=%7B%22screen_name%22%3A%22" + screen_name + "%22%2C%22withSafetyModeUserFields%22%3Atrue%7D&features=%7B%22hidden_profile_likes_enabled%22%3Afalse%2C%22responsive_web_graphql_exclude_directive_enabled%22%3Atrue%2C%22verified_phone_label_enabled%22%3Afalse%2C%22subscriptions_verification_info_verified_since_enabled%22%3Atrue%2C%22highlights_tweets_tab_ui_enabled%22%3Atrue%2C%22creator_subscriptions_tweet_preview_api_enabled%22%3Atrue%2C%22responsive_web_graphql_skip_user_profile_image_extensions_enabled%22%3Afalse%2C%22responsive_web_graphql_timeline_navigation_enabled%22%3Atrue%7D"
        client.get({
            url: twurl,
            headers: headers
        }).then((data) => {
            try {
                result = JSON.parse(data.body)
                if (result.length !== 0) {
                    selfId = result.data.user.result.rest_id
                    return
                }
            } catch (e) {
                return
            }
        })

        setTimeout(() => {
            if (share_blockList === undefined) {
                return
            }
            blockList = share_blockList.split('\n')
            blockListTmp = share_blockList.split('\n')
            blockList.forEach((item) => {
                if (item !== '') {
                    shareBlockTweet(JSON.stringify(item), (data) => {
                        if (data.body === "1") {
                            index = blockListTmp.indexOf(item)
                            blockListTmp.splice(item, index)
                        }
                    })

                }
            })
            share_blockList = blockListTmp.join('\n')
            chrome.storage.sync.set({
                'share_blockList': share_blockList
            })
        }, 10000)

        const config = { attributes: true, childList: true, subtree: true, characterData: true }
        watchDOM(document, config)
    }, 3000)
}

try {
    main()
} catch (error) {
    console.log("main error", error)
}