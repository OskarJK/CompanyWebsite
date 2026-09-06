# Beauty & Hair Salon Web Application

A commercial full-stack web application built for a luxury beauty salon. The platform serves as a modern digital showcase and service catalog, allowing clients to browse treatments, view detailed pricing and durations, and initiate direct appointment bookings across mobile and desktop devices.

---

## Tech Stack

| Layer | Technologies |
|-------|-------------|
| Backend | Python, Django, PostgreSQL / SQLite |
| Frontend | HTML5, CSS3 (Custom Properties, Grid, Flexbox), Vanilla JavaScript (ES6+) |
| Security | Form Honeypot Anti-Spam, Environment Variable Isolation (`python-dotenv`) |
| Integrations | Treatwell Booking, WhatsApp Click-to-Chat, SMTP Email Services |
| Infrastructure | Docker, Docker Compose, Gunicorn |

---

## Features

- **Interactive Service Showcase:** Category-based service catalog with real-time filtering and modal popups for pricing and treatment details.
- **Conversion-Driven Booking:** Seamless integration with Treatwell scheduling and direct WhatsApp click-to-chat messaging.
- **Instant Email Notifications:** Integrated Django SMTP backend dispatching automated, responsive HTML notification emails directly to the salon's inbox upon form submission.
- **Mobile-Optimized UX:** Custom CSS layout engine engineered for smooth 60fps scrolling, resolving background render bottlenecks on smartphones.
- **Frictionless Spam Protection:** Custom Honeypot form security that filters automated bot submissions without forcing human users to complete annoying reCAPTCHAs.
- **Dynamic Content Management:** Highly customized Django Admin panel with restricted permissions, enabling non-technical staff to safely update treatments, prices, and media.
- **DACH/EU Legal Compliance:** Built-in GDPR privacy checkmarks, structured legal footers (Impressum & Datenschutz), and inquiry status tracking.

---

## What a Visitor Can Do

- **Explore Treatment Offerings:** Filter services by category (e.g., Haircuts, Styling, Nails) without reloading the page.
- **View Full Treatment Details:** Click on any service card to open a detailed modal with complete descriptions and prices.
- **Book Appointments:** Reserve slots immediately through Treatwell or contact the salon directly via WhatsApp.
- **Send Direct Inquiries:** Submit messages through a secure contact form with instant email notification delivery to the business.
- **Locate the Salon:** View operating hours, dual location details, and direct links to interactive Google Maps.
- **Review Legal Information:** Access required business disclosures and EU dispute resolution links directly from the page footer.

---

## The Process

The application was designed to solve a direct business problem: replacing static social media profiles with an owned, high-performing digital platform. The project began by translating the salon owner's requirements into relational Django database models for treatment categories, individual services, company metadata, and incoming inquiry logs.

Rather than introducing heavy frontend frameworks, the client interface was built using semantic HTML, modern CSS, and modular Vanilla JavaScript to ensure minimal bundle sizes and instant initial load times. During mobile usability testing, rendering stutter caused by fixed backgrounds was identified and resolved using GPU-accelerated CSS layer techniques (`will-change: transform`). 

To ensure seamless client communication, Django's transactional email backend was integrated. It securely processes contact forms, sanitizes the inputs, and forwards beautiful HTML-formatted emails instantly to the salon's inbox, with robust fallback error handling to protect the user experience. To finalize the project for deployment, sensitive configuration settings and SMTP credentials were isolated into `.env` variables, and the entire application lifecycle was containerized using Docker Compose.

---

## What I Learned

- **Commercial Client Workflow:** Gathering business requirements from a non-technical stakeholder and translating them into solid database architecture.
- **Transactional Email Integration:** Setting up Django's SMTP email service to construct and route dynamic HTML inquiries directly to business email accounts with proper error handling.
- **Mobile Rendering Performance:** Diagnosing browser paint bottlenecks and applying GPU hardware acceleration to maintain high frame rates during scroll interactions.
- **Vanilla JS Architecture:** Building lightweight, stateful UI components (modals, active tabs) without external JavaScript framework dependencies.
- **UX-Friendly Form Security:** Implementing Honeypot anti-spam techniques and required privacy booleans in Django forms to protect backends without frustrating human users.
- **Admin Panel Customization:** Modifying Django Admin permissions (`has_add_permission`, `get_readonly_fields`) to prevent data duplication and protect application integrity.

---

## How It Could Be Improved

- **Online Payment Processing:** Integrate Stripe or PayPal SDKs to accept deposit payments during online bookings.
- **SMS Notifications:** Integrate SMS gateway APIs (e.g., Twilio) to send instant SMS booking alerts directly to staff mobile phones.
- **Automated Media Optimization:** Implement background image processing using Pillow to automatically resize and convert uploaded service photos into WebP format.
- **Multi-Language Support (i18n):** Add German, Polish, and English locale switching using Django's built-in internationalization engine.
- **CI/CD Pipeline:** Automate testing, linting, and deployment tasks via GitHub Actions.
