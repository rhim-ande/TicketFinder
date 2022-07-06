GET /discovery/v2/events.json?apikey={HYTeCD8nCfFuOtQog8WunqWnAgA5eS1g}&size=1 HTTP/1.1
Host: app.ticketmaster.com
X-Target-URI: https://app.ticketmaster.com
Connection: Keep-Alive


url:"https://app.ticketmaster.com/discovery/v2/events.json?size=1&apikey={HYTeCD8nCfFuOtQog8WunqWnAgA5eS1g}"

response = requests.get(url)
