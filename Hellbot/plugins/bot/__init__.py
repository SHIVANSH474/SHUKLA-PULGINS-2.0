from Hellbot.core.clients import hellbot
from Hellbot.core.config import Config, Symbols
from Hellbot.core.database import db
from Hellbot.plugins.help import BotHelp
from Hellbot.plugins.USERBOTDEPLOY import USERBOTDEPLOY


START_MSG = """
👋 **𝖦𝗋𝖾𝖾𝗍𝗂𝗇𝗀𝗌, {0} - 𝗐𝖺𝗋𝗋𝗂𝗈𝗋𝗌 𝗈𝖿 Pbxbot 2.0!** 👹 𝖨 𝖺𝗆 𝗒𝗈𝗎𝗋 𝗍𝗋𝗎𝗌𝗍𝗒 𝖼𝗈𝗆𝗉𝖺𝗇𝗂𝗈𝗇, 𝗍𝗁𝖾 **Pbxbot 2.0 𝖠𝗌𝗌𝗂𝗌𝗍𝖺𝗇𝗍!** 🚀

👋🏻ɪ ᴀᴍ ᴀᴅᴠᴀɴᴄᴇᴅ ⛏ ᴀɴᴅ sᴜᴘᴇʀғᴀsᴛ ⛓ᴛᴇʟᴇɢʀᴀᴍ  ᴘʙx 2.0 ᴜsᴇʀʙᴏᴛ 🤖 .
🦋ᴡʜᴇᴛʜᴇʀ ɪᴛ's ᴄʀᴇᴀᴛɪɴɢ, ᴅᴇʟᴇᴛɪɴɢ 🚫 ᴏʀ ᴜᴘᴅᴀᴛɪɴɢ 🔧 ʏᴏᴜʀ ᴜsᴇʀʙᴏᴛ, ɪ'ᴠᴇ ɢᴏᴛ ʏᴏᴜʀ ʙᴀᴄᴋ 🧹.
💀ᴍᴀʏ ʏᴏᴜʀ ᴄᴏᴍᴍᴀɴᴅs 📲 ʙᴇ sᴡɪғᴛ ᴀɴᴅ ʏᴏᴜʀ sᴇssɪᴏɴ ʟᴇɢᴇɴᴅᴀʀʏ ☠.

**𝖶𝖾𝗅𝖼𝗈𝗆𝖾 𝗍𝗈 Pbxbot 2.0 𝖠𝗌𝗌𝗂𝗌𝗍𝖺𝗇𝗍 – 𝗐𝗁𝖾𝗋𝖾 Pbxbot 2.0 𝗅𝖾𝗀𝖺𝖼𝗒 𝗅𝗂𝗏𝖾𝗌 𝗈𝗇 🤖!**

**❤️ @ll_THE_BAD_BOT_ll ❤️**
"""

HELP_MSG = """
**⚙️ 𝖧𝖾𝗅𝗉★**

**__» All commands are categorized and you can use these buttons below to navigate each category and get respective commands.__
__» Feel free to contact us if you need any help regarding the bot.__**

**❤️ @ll_THE_BAD_BOT_ll ❤️**
  
  **★USERBOT DEPLOY★**

**since i never mentioned how to activate userbot on your account. here's a little guide.

1. deployment is successful and bot is working .

2. send /session to your helper bot.

3. now click on "new" button and add your account.

4. follow all the prompts and do the needful.

5. restart the bot with /restart command.**

**❤️ @ll_THE_BAD_BOT_ll ❤️**
"""
USERBOTDEPLOY = """
**★USERBOT DEPLOY★**



since i never mentioned how to activate userbot on your account. here's a little guide.

1. deployment is successful and bot is working .

2. send /session to your helper bot.

3. now click on "new" button and add your account.

4. follow all the prompts and do the needful.

5. restart the bot with /restart command.

**❤️ @ll_THE_BAD_BOT_ll ❤️**
"""
