// ============================================
// Kelvin Uduma — Portfolio Scripts
// ============================================

document.addEventListener("DOMContentLoaded", () => {
  // --- Navbar scroll effect ---
  const nav = document.getElementById("nav");
  let lastScroll = 0;

  window.addEventListener("scroll", () => {
    const currentScroll = window.pageYOffset;
    if (currentScroll > 60) {
      nav.classList.add("scrolled");
    } else {
      nav.classList.remove("scrolled");
    }
    lastScroll = currentScroll;
  });

  // --- Mobile nav toggle ---
  const navToggle = document.getElementById("navToggle");
  const navLinks = document.querySelector(".nav-links");

  if (navToggle) {
    navToggle.addEventListener("click", () => {
      navLinks.style.display =
        navLinks.style.display === "flex" ? "none" : "flex";
      if (window.innerWidth <= 768) {
        navLinks.style.position = "absolute";
        navLinks.style.top = "100%";
        navLinks.style.left = "0";
        navLinks.style.right = "0";
        navLinks.style.flexDirection = "column";
        navLinks.style.padding = "24px";
        navLinks.style.background = "rgba(10, 14, 26, 0.98)";
        navLinks.style.borderBottom = "1px solid rgba(139, 147, 167, 0.12)";
        navLinks.style.backdropFilter = "blur(20px)";
      }
    });
  }

  // Close mobile nav on link click
  document.querySelectorAll(".nav-links a").forEach((link) => {
    link.addEventListener("click", () => {
      if (window.innerWidth <= 768) {
        navLinks.style.display = "none";
      }
    });
  });

  // --- Scroll-reveal animations ---
  const observerOptions = {
    root: null,
    rootMargin: "0px 0px -60px 0px",
    threshold: 0.1,
  };

  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("revealed");
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);

  // Observe all cards and sections
  const revealElements = document.querySelectorAll(
    ".highlight-card, .expertise-card, .project-card, .credential-card, .section-title, .about-lead, .contact-block",
  );

  revealElements.forEach((el) => {
    el.style.opacity = "0";
    el.style.transform = "translateY(30px)";
    el.style.transition = "opacity 0.6s ease, transform 0.6s ease";
    observer.observe(el);
  });

  // Add stagger delay to grid items
  document
    .querySelectorAll(
      ".expertise-grid, .projects-grid, .credentials-grid, .about-highlights",
    )
    .forEach((grid) => {
      const children = grid.children;
      Array.from(children).forEach((child, i) => {
        child.style.transitionDelay = `${i * 0.1}s`;
      });
    });

  // CSS class for revealed state
  const style = document.createElement("style");
  style.textContent = `.revealed { opacity: 1 !important; transform: translateY(0) !important; }`;
  document.head.appendChild(style);

  // --- Smooth anchor scrolling (fallback) ---
  document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
    anchor.addEventListener("click", function (e) {
      const href = this.getAttribute("href");
      if (href === "#") return;
      e.preventDefault();
      const target = document.querySelector(href);
      if (target) {
        target.scrollIntoView({ behavior: "smooth", block: "start" });
      }
    });
  });

  // --- Modal Logic ---
  const modals = document.querySelectorAll(".modal");
  const overlay = document.getElementById("modalOverlay");
  const closeButtons = document.querySelectorAll(".modal-close");

  // Make project cards clickable to open modals
  const projectMap = {
    "ISM Code ↔ NIST CSF 2.0 Crosswalk": "modal-crosswalk",
    "JCL Safety Management System": "modal-sms",
    "Cybersecurity Policy Suite": "modal-cyber",
    "IT Infrastructure Portfolio": "modal-it",
    "Budget Link Integrity Checker": "modal-budget",
    "SmartVessel Deployment": "modal-smartvessel",
    "Microsoft Graph MCP Server": "modal-mcp",
  };

  document.querySelectorAll(".project-card").forEach((card) => {
    card.addEventListener("click", () => {
      const titleElement = card.querySelector("h3");
      if (titleElement) {
        const title = titleElement.textContent.trim();
        const modalId = projectMap[title];
        if (modalId) {
          const modal = document.getElementById(modalId);
          if (modal) {
            modal.classList.add("active");
            overlay.classList.add("active");
            document.body.style.overflow = "hidden";
          }
        }
      }
    });
  });

  const closeModal = () => {
    modals.forEach((m) => m.classList.remove("active"));
    if (overlay) overlay.classList.remove("active");
    document.body.style.overflow = "";
  };

  closeButtons.forEach((btn) =>
    btn.addEventListener("click", (e) => {
      e.stopPropagation();
      closeModal();
    }),
  );

  if (overlay) {
    overlay.addEventListener("click", closeModal);
  }
});
