# League of Legends champion picker
This project allows players to create the best possible team using statistics from the Champion.gg and Riot APIs.

## API Endpoints

### Champions
```
GET /api/champions/
```
List all champions in the database.

```
GET /api/champions/{id}/
```
Get stats for the specified champion.

```
GET /api/champions/{id}/roles/
```
Get all roles associated with the specified champion id.

### Roles
```
GET /api/roles/
```
Get all champions' roles and associated stats.

```
GET /api/roles/{id}/
```
Get a specific role.

### Items
```
GET /api/items/
```
List all items.

```
GET /api/items/{id}/
```
Get stats for the specified item.

```
GET /api/builds/
```
Get all item builds.

```
GET /api/builds/{id}/
```
Get a specific item build.

### Matchups

```
POST /matchups/
```

The matchups API expects a JSON body of the following format:
```
{
    "bans": ["Champion", ...],
    "team1": ["Champion", ...],
    "team2": ["Champion", ...],
    "team": 1,
}
```
`bans`, `team1`, and `team2` are arrays of champion names that are selected for each part of champion select. `team` indicates the team that is currently selecting a champion. The response is a list of counters for the enemy's champions that are available to be selected.
