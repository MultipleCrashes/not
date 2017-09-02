import notify2

IMAGE_PATH = ''

notify2.init('Notifier')
n = notify2.Notification(None, icon = IMAGE_PATH)
n.set_urgency(notify2.URGENCY_NORMAL)
n.set_timeout(10000)

n.update('New message', 'From Notfieir')
n.show()



