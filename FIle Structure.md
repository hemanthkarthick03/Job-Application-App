job_portal/
│
├── backend/
│   ├── app.py               # Main application file
│   ├── config.py            # Configuration settings (DB URI, JWT secret, etc.)
│   ├── models.py            # SQLAlchemy models
│   ├── routes/
│   │   ├── auth.py          # Authentication routes (login, register)
│   │   ├── jobs.py          # Job-related routes (CRUD operations)
│   │   ├── applications.py  # Application-related routes
│   ├── services/
│   │   ├── auth_service.py   # Authentication logic (token generation, etc.)
│   │   ├── job_service.py    # Business logic for job postings
│   │   ├── application_service.py  # Business logic for applications
│   ├── migrations/          # Database migrations
│   ├── tests/               # Unit tests
│   └── utils.py             # Utility functions (e.g., token validation)
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   │   ├── Auth/        # Login, Register components
│   │   │   ├── Job/         # Job listings, Job detail, Create/Edit job components
│   │   │   ├── Application/ # Application forms, View applications
│   │   ├── context/
│   │   │   ├── AuthContext.js  # Context for managing authentication state
│   │   ├── hooks/
│   │   │   ├── useAuth.js   # Custom hook for authentication logic
│   │   ├── pages/
│   │   │   ├── Home.js      # Home page
│   │   │   ├── Dashboard.js # Employer/Candidate dashboard
│   │   ├── services/
│   │   │   ├── api.js       # Axios instance and API calls
│   │   ├── App.js           # Main app component with routing
│   │   ├── index.js         # Entry point for React
│   ├── .env                 # Environment variables (API URLs)
│   ├── package.json         # Dependencies and scripts
│
└── README.md                # Project overview and setup instructions


// Frontend:

frontend/
├── public/
├── src/
│   ├── components/
│   │   ├── Auth/
│   │   │   ├── Login.js
│   │   │   ├── Register.js
│   │   ├── Job/
│   │   │   ├── JobDetail.js
│   │   │   ├── JobList.js
│   │   │   ├── PostJob.js
│   │   ├── Application/
│   │   │   ├── ApplyJob.js
│   │   │   ├── MyApplications.js
│   │   ├── Dashboard/
│   │   │   ├── EmployerDashboard.js
│   │   │   ├── CandidateDashboard.js
│   ├── context/
│   │   ├── AuthContext.js
│   ├── hooks/
│   │   ├── useAuth.js
│   ├── pages/
│   │   ├── Home.js
│   │   ├── Dashboard.js
│   ├── App.js
│   ├── index.js
│
└── README.md
