WelcomeText = \
"""
𝐇𝐢! **%(first_name)s**, 𝐬𝐞𝐧𝐝 𝐦𝐞 𝐚𝐧𝐲 𝐟𝐢𝐥𝐞 𝐭𝐨 𝐠𝐞𝐭 𝐚 𝐝𝐢𝐫𝐞𝐜𝐭 𝐬𝐭𝐫𝐞𝐚𝐦𝐛𝐥𝐞 𝐥𝐢𝐧𝐤 𝐭𝐨 𝐭𝐡𝐚𝐭 𝐟𝐢𝐥𝐞 🍿.
"""

UserInfoText = \
"""
**First Name:**
`{sender.first_name}`

**Last Name:**
`{sender.last_name}`

**User ID:**
`{sender.id}`

**Username:**
`@{sender.username}`
"""

FileLinksText = \
"""
**Download Link:**
`%(dl_link)s`
**Telegram File:**
`%(tg_link)s`
"""

MediaLinksText = \
"""
**Download Link:**
`%(dl_link)s`
**Stream Link:**
`%(stream_link)s`
**Telegram File:**
`%(tg_link)s`
"""

InvalidQueryText = \
"""
Query data mismatched.
"""

MessageNotExist = \
"""
File revoked or not exist.
"""

LinkRevokedText = \
"""
The link has been revoked. It may take some time for the changes to take effect.
"""

InvalidPayloadText = \
"""
Invalid payload.
"""

MediaTypeNotSupportedText = \
"""
Sorry, this media type is not supported.
"""
