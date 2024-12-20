import MailCow

moo = MailCow()
logs = moo.getRequest(section='logs/api/5')
moo.data = logs
print(moo.as_table())

# igy kene kinezzen 
moo.getAllMailboxes()