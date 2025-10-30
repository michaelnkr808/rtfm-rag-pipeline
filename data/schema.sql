-- RTFM Database Schema
-- 
-- Table Relationships:
-- - users.server_id → servers.server_id (Foreign Key)
-- - Relationship Type: One-to-Many (one server has many users)
-- - Cascade Behavior: Deleting a server deletes all associated users

CREATE TABLE servers (
    server_id VARCHAR(255) PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    config JSONB
);

CREATE TABLE users (
    user_id VARCHAR(255) PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    server_id VARCHAR(255) REFERENCES server(server_id) ON DELETE CASCADE
)