# ctftime_ratings
rate notifier

config.json:
```
{
  "teams": [
    { "id": your_team_id_here }
  ]
}
```

```
$ ./check.py
scryptos: 54th (228.273082)
```

```
$ ./notify # post to slack (ignore if the message is already recorded)
slackcat message sent to general (0.295s)
```
- https://github.com/193s/slackcat

![image](https://cloud.githubusercontent.com/assets/6814758/13628509/fefe22b6-e615-11e5-9e83-703ceb4498fb.png)

