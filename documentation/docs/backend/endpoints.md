# API Endpoints

## Team Endpoint

#### Model Attributes

- `team_id`
- `name`
- `join_code`
- `bio`

#### Views

- `create_team/` - Create a new team
- `get_teams/` - Retrieve a list of teams
- `get_teams/<int:team_id>` - Retrieve a team by id
- `update_team/<int:team_id>` - Update a team by id
- `delete_team/<int:team_id>` - Delete a team by id

## Event Endpoint

#### Model Attributes

- `event_id`
- `name`
- `start_date`
- `end_date`
- `description`
- `is_public`
- `team_id` [Optional]
- `is_archived`

#### Views

- `create_event/` - Create a new event
- `get_events/` - Retrieve a list of events
- `get_events/<int:event_id>` - Retrieve an event by id
- `update_event/<int:event_id>` - Update an event by id
- `delete_event/<int:event_id>` - Delete an event by id

## Subteam Endpoint

#### Model Attributes

- `subteam_id`
- `name`
- `team_id`

#### Views

- `create_subteam/` - Create a new subteam
- `get_subteams/<int:team_id>` - Retrieve a subteam by team_id
- `update_subteam/<int:subteam_id>` - Update a subteam by id
- `delete_subteam/<int:subteam_id>` - Delete a subteam by id

## Mileage Endpoint

#### Model Attributes

- `mileage_id`
- `user_id`
- `kilometers`
- `date`

#### Views

- `create_mileage/` - create new mileage
- `get_mileage/<int:user_id>` - Retrieve a list of mileage by user_id

## User Endpoint

#### Model Attributes

- `id`
- `username`
- `first_name`
- `last_name`
- `email`
- `team_signup`
- `has_consent`
- `avatar`
- `travel_method`
- `team_id` [Optional]
- `subteam_id` [Optional]
- `team_admin` [Optional]
