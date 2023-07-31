# API Endpoints

## Team Endpoint

#### Model Attributes

- `team_id`
- `name`
- `join_code`
- `bio`
- `total_mileage`

#### Views

- `create/` - Create a new team
- `get_teams/` - Retrieve a list of teams
- `get/<int:team_id>` - Retrieve a team by id
- `edit/<int:team_id>` - Update a team by id
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

- `create/` - Create a new event
- `get/` - Retrieve a list of events
- `update/<int:event_id>` - Update an event by id
- `delete/<int:event_id>` - Delete an event by id

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
- `get_users/<int:subteam_id>` - Get users by subteam id
- `get_available_users/` - Get users that have no subteam
- `edit_user/<int:user_id>` - Change user subteam
- `delete_user_from_subteam/<int>:user_id>` - Remove an user from subteam
-

## Mileage Endpoint

#### Model Attributes

- `mileage_id`
- `user_id`
- `kilometers`
- `date`
- `team`

#### Views

- `get_leaderboard/` - Returns leaderboard data
- `get_mileage` - Returns a list of mileage
- `post_mileage` - Add mileage

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
- `reset_token` [Optional]
- `reset_time` [Optional]
- `challenge_start_date` [Optional]
- `total_mileage` [Optional]
