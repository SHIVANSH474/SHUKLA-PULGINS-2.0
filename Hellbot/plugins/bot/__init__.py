from Hellbot.core.clients import hellbot
from Hellbot.core.config import Config, Symbols
from Hellbot.core.database import db
from Hellbot.plugins.help import BotHelp


START_MSG = """
👋 **𝖦𝗋𝖾𝖾𝗍𝗂𝗇𝗀𝗌, {0} - 𝗐𝖺𝗋𝗋𝗂𝗈𝗋𝗌 𝗈𝖿 Pbxbot 2.0!** 👹 𝖨 𝖺𝗆 𝗒𝗈𝗎𝗋 𝗍𝗋𝗎𝗌𝗍𝗒 𝖼𝗈𝗆𝗉𝖺𝗇𝗂𝗈𝗇, 𝗍𝗁𝖾 **Pbxbot 2.0 𝖠𝗌𝗌𝗂𝗌𝗍𝖺𝗇𝗍!** 🚀

𝖧𝖾𝗋𝖾 𝗍𝗈 𝗌𝖾𝗋𝗏𝖾, 𝗀𝗎𝗂𝖽𝖾, 𝖺𝗇𝖽 💪 𝗎𝗇𝗅𝖾𝖺𝗌𝗁 𝗍𝗁𝖾 𝗉𝗈𝗐𝖾𝗋 𝗈𝖿 Pbxbot 2.0 𝖺𝗍 𝗒𝗈𝗎𝗋 𝖼𝗈𝗆𝗆𝖺𝗇𝖽! 🎉
𝖶𝗁𝖾𝗍𝗁𝖾𝗋 𝗂𝗍'𝗌 𝖼𝗋𝖾𝖺𝗍𝗂𝗇𝗀, 𝖽𝖾𝗅𝖾𝗍𝗂𝗇𝗀, 𝗈𝗋 𝗎𝗉𝖽𝖺𝗍𝗂𝗇𝗀 𝗒𝗈𝗎𝗋 𝗎𝗌𝖾𝗋𝖻𝗈𝗍, 𝖨'𝗏𝖾 𝗀𝗈𝗍 𝗒𝗈𝗎𝗋 𝖻𝖺𝖼𝗄.
𝖢𝗈𝗇𝗌𝗂𝖽𝖾𝗋 𝗆𝖾 𝗒𝗈𝗎𝗋 𝗉𝖾𝗋𝗌𝗈𝗇𝖺𝗅 𝗌𝗂𝖽𝖾𝗄𝗂𝖼𝗄 🤭 𝗂𝗇 𝗍𝗁𝖾 𝗋𝖾𝖺𝗅𝗆 𝗈𝖿 𝗎𝗅𝗍𝗂𝗆𝖺𝗍𝖾 𝗎𝗌𝖾𝗋𝖻𝗈𝗍 𝗆𝖺𝗌𝗍𝖾𝗋𝗒.

🍀 𝖫𝖾𝗍'𝗌 𝖾𝗆𝖻𝖺𝗋𝗄 𝗈𝗇 𝗍𝗁𝗂𝗌 𝖾𝗉𝗂𝖼 𝗃𝗈𝗎𝗋𝗇𝖾𝗒 𝗍𝗈𝗀𝖾𝗍𝗁𝖾𝗋!
𝖨𝖿 𝗒𝗈𝗎 𝖾𝗏𝖾𝗋 𝗇𝖾𝖾𝖽 𝖺𝗌𝗌𝗂𝗌𝗍𝖺𝗇𝖼𝖾 𝗈𝗋 𝖼𝗋𝖺𝗏𝖾 ✨ 𝗍𝗁𝖾 𝗍𝗁𝗋𝗂𝗅𝗅 𝗈𝖿 𝗎𝗇𝗅𝖾𝖺𝗌𝗁𝗂𝗇𝗀 Pbxbot 2.0 𝗆𝗂𝗀𝗁𝗍, 𝗃𝗎𝗌𝗍 𝗌𝗎𝗆𝗆𝗈𝗇 𝗆𝖾.
𝖶𝖾'𝗋𝖾 𝖺𝖻𝗈𝗎𝗍 𝗍𝗈 𝖼𝗈𝗇𝗊𝗎𝖾𝗋 𝗇𝖾𝗐 𝗁𝖾𝗂𝗀𝗁𝗍𝗌 🚀 𝗂𝗇 𝗍𝗁𝖾 𝗎𝗌𝖾𝗋𝖻𝗈𝗍 𝗎𝗇𝗂𝗏𝖾𝗋𝗌𝖾!

💫 𝖬𝖺𝗒 𝗒𝗈𝗎𝗋 𝖼𝗈𝗆𝗆𝖺𝗇𝖽𝗌 𝖻𝖾 𝗌𝗐𝗂𝖿𝗍 𝖺𝗇𝖽 𝗒𝗈𝗎𝗋 𝗌𝖾𝗌𝗌𝗂𝗈𝗇𝗌 𝗅𝖾𝗀𝖾𝗇𝖽𝖺𝗋𝗒.
**𝖶𝖾𝗅𝖼𝗈𝗆𝖾 𝗍𝗈 Pbxbot 2.0 𝖠𝗌𝗌𝗂𝗌𝗍𝖺𝗇𝗍 – 𝗐𝗁𝖾𝗋𝖾 Pbxbot 2.0 𝗅𝖾𝗀𝖺𝖼𝗒 𝗅𝗂𝗏𝖾𝗌 𝗈𝗇 🤖!**
"""

HELP_MSG = """
**⚙️ 𝖧𝖾𝗅𝗉★**

__» All commands are categorized and you can use these buttons below to navigate each category and get respective commands.__
__» Feel free to contact us if you need any help regarding the bot.__

**❤️ @ll_THE_BAD_BOT_ll ❤️**
  
"""USERBOT_DEPLOY ="""
**★USERBOT DEPLOY★**

since i never mentioned how to activate userbot on your account. here's a little guide.

1. After deployment is successful and bot is working you'll need to start the helper bot.

2. send /session to your helper bot.

3. now click on "new" button and add your account.

4. follow all the prompts and do the needful.

5. restart the bot with /restart command.

**❤️ @ll_THE_BAD_BOT_ll ❤️**
"""
