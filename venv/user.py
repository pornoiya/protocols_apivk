from script import VK_App
import webbrowser
import os
import argparse


class GoodLookingResult:
    @staticmethod
    def build_page(str):
        html_text = """<!DOCTYPE html>
                        <html lang="ru">
                        <head>
                        <title>vkapi_result</title>
                        <meta charset="UTF-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1">
                        <style>
                        /* Style the body */
                        body {
                          font-family: Georgia;
                          margin: 0;
                        }

                        /* Header/Logo Title */
                        .header {
                          padding: 60px;
                          text-align: center;
                          background: #1abc9c;
                          color: white;
                          font-size: 30px;
                        }

                        /* Page Content */
                        .content {padding:20px;}
                        </style>
                        </head>
                        <body>

                        <div class="header">
                          <p>i've just got user's friends by vk's API.</p>
                          <p>here they are:</p>
                        </div>

                        <div class="content">
                          <h1>friends list:</h1>
                          %s
                        </div>

                        </body>
                        </html>
                        """ % str
        with open(os.getcwd() + "friend_list.html", 'w', encoding="utf-8") as f:
            f.write(html_text)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-uid", required=True,
                        help="id or domain screen name of user\nexample: -id 122344 OR -id id56567 OR -id pornoiya")
    parser.add_argument("-aid", required=True, help="id of vk application")
    parser.add_argument("-tkn", required=True, help="access token of vk application")
    cnsl_args = parser.parse_args().__dict__
    protocols_app = VK_App(cnsl_args["aid"], cnsl_args["tkn"])
    user_id = cnsl_args["uid"]
    rep = protocols_app.get_friends_list(user_id)['items']
    res = "\n".join(["<p>" + f'<a href="https://vk.com/id{repl["id"]}">'
                     + repl['last_name'] + " " + repl['first_name']
                     + "</a>" + "</p>" for repl in rep])
    GoodLookingResult.build_page(res)
    url = os.getcwd() + "friend_list.html"
    webbrowser.open(url, new=1)

