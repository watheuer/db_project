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
