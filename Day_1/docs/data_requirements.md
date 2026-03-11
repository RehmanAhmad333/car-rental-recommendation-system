# Data Requirements Specification

## Overview
The recommendation system requires data from the car rental application database.

Primary data sources include:

- Cars Collection
- Users Collection
- Bookings Collection

---

## Cars Dataset

Fields required:

| Field | Description |
|------|-------------|
| carId | Unique identifier |
| name | Car model |
| brand | Car manufacturer |
| category | Vehicle category |
| pricePerDay | Rental price |
| description | Vehicle description |
| availability | Availability status |

Purpose:
Used for Content-Based Filtering.

---

## Users Dataset

| Field | Description |
|------|-------------|
| userId | Unique identifier |
| name | User name |
| email | User email |
| createdAt | Registration date |

Purpose:
Used for tracking user preferences.

---

## Bookings Dataset

| Field | Description |
|------|-------------|
| bookingId | Unique booking |
| userId | User reference |
| carId | Car reference |
| startDate | Booking start |
| endDate | Booking end |
| totalPrice | Total price |
| status | Booking status |

Purpose:
Used for Collaborative Filtering.

---

## Data Format

Expected format:

- MongoDB JSON
- CSV export for ML training

---

## Data Preprocessing Requirements

- Remove missing values
- Convert categorical data to numeric format
- Normalize price features
- Clean text descriptions