import socket

params = "headers=SG9zdDogd3d3Lmdvb2dsZS5jb20NClVzZXItQWdlbnQ6"\
         "IE1vemlsbGEvNS4wIChNYWNpbnRvc2g7IEludGVsIE1hYyBPUyBY"\
         "IDEwLjY7IHJ2OjIuMC4xKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94"\
         "LzQuMC4xDQpBY2NlcHQ6IHRleHQvaHRtbCxhcHBsaWNhdGlvbi94"\
         "aHRtbCt4bWwsYXBwbGljYXRpb24veG1sO3E9MC45LCovKjtxPTAu"\
         "OA0KQWNjZXB0LUxhbmd1YWdlOiBlbi11cyxlbjtxPTAuNQ0KQWNj"\
         "ZXB0LUVuY29kaW5nOiBnemlwLCBkZWZsYXRlDQpBY2NlcHQtQ2hh"\
         "cnNldDogSVNPLTg4NTktMSx1dGYtODtxPTAuNywqO3E9MC43DQpL"\
         "ZWVwLUFsaXZlOiAxMTUNClByb3h5LUNvbm5lY3Rpb246IGtlZXAt"\
         "YWxpdmUNCkNvb2tpZTogUFJFRj1JRD02NGU2MGE4ODUxNzEyZDkw"\
         "OlU9ZDgzY2M5YjQ5NmY5YWViZTpUTT0xMzA1MDE3NjI1OkxNPTEz"\
         "MDUwODE1MDI6R009MTpTPW8wbEtfTnVtbkV6TjZFSnM7IHJlbWVt"\
         "YmVybWU9dHJ1ZTsgTklEPTQ2PU5pU3RIcmozVFBINjYzZjFmTzB5"\
         "eEdYSWRlUXhWUW9WNlRjOWZqd2FIUDFPQjRfSjJBSklfc2hlTzE0"\
         "dHhCZGdpOUwtblpnWUxaWWp0OFNSMnRhYjF3el9Oc0ZQMTk4NURF"\
         "VVdTZ0F6aTlxVzhHNm4yNk84UFhnSUMyNndWRWtwOyBTSUQ9RFFB"\
         "QUFMVUFBQUJZZ01Zdk04eXZJY1JKV1d3eU14U3Y1ZmVVM1JVSlNK"\
         "ekdYVzVWajIySW9EWnctYmpnWkh2OXNXX0k5djAyMWhnM3RoQlJx"\
         "QmE1WjhlNTJTOXZaM0pKc0tpeWNHZUNvWms4alY1VVZOdmZyd1dX"\
         "aER2MU1nbksySVc0YnRPM3NWZU05YlZnVjNxZDNiZHhVVl9ndTRM"\
         "ekpfdXk4V3NWdjczYlV4Y1V3dXNpNHV6S0ZQVXJCYUFzSTc3QWJp"\
         "YkEybVNIdV9NQXUtWFRiaUI5NlVSbTNfc091QUxHTjJLT3U0N19q"\
         "MmdEN1psYUlxdmpkNkppdzk3SEdyZ01oRHdSd1hNOyBIU0lEPUF4"\
         "c1JtTkpxUG9sQW1Ic21kOyBUWj0tNDgwDQpDYWNoZS1Db250cm9s"\
         "OiBtYXgtYWdlPTANCg%3D%3D&version=2.0.0&encoded_path="\
         "aHR0cDovL3d3dy5nb29nbGUuY29tLw%3D%3D&method=GET&post"\
         "data="

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("www.google.cn", 80))
sock.send("%s %s\r\n" % ("GET", "http://[gae_app_name].appspot.com/fetch.py?" + params))

received = ""
while True:
    data = sock.recv(8192)
    if data != "":
        received += data
    else:
        # EOF
        break

# clean
sock.close()

print received

