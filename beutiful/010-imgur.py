import requests as req


url = "https://webhook.site/ff20c4f0-45c7-4d0d-84b9-0bf49de4dd11"

res = req.post(url, data={
  "name":"hi"
})
