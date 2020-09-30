import pandas

# Making an empty dataframe for logging the coordinates
log = pandas.DataFrame(columns=["Count", "Snake_x", "Snake_y", "Snake_angle"])
# Making a counter
counter = 11

#log["Snake_x"][0]

log = pandas.DataFrame(columns=["Count", "Snake_x", "Snake_y", "Snake_angle"])
for i in range(1,12):
    log = log.append({
        "Count": i,
        "Snake_x": 480,
        "Snake_y": 320,
        "Snake_angle": 0
    }, ignore_index=True)

tail_x = log["Snake_x"][log["Count"][counter - 11]]
tail_y = log["Snake_y"][log["Count"][counter - 11]]
tail_angle = log["Snake_y"][log["Count"][counter - 11]]


print(len(log))
log = log.drop(0)
print(len(log))