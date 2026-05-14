import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Add favicon
html = html.replace('</head>', '    <link rel="icon" type="image/svg+xml" href="favicon.svg">\n</head>')

# Add Resume Button
hero_actions = """            <div class="hero-actions">
                <a href="#projects" class="btn btn-primary">View My Work</a>
                <a href="Kelvin_Uduma_Resume.pdf" class="btn btn-secondary" download>Download CV</a>"""
html = re.sub(r'            <div class="hero-actions">\s*<a href="#projects" class="btn btn-primary">View My Work</a>', hero_actions, html)

# Make project cards clickable
projects_map = {
    "JCL Safety Management System": "sms",
    "Cybersecurity Policy Suite": "cyber",
    "IT Infrastructure Portfolio": "it",
    "Budget Link Integrity Checker": "budget",
    "SmartVessel Deployment": "smartvessel",
    "Papaya Genetic Diversity Research": "papaya",
    "Outlook + OneDrive MCP Server": "mcp"
}

for title, pid in projects_map.items():
    # Find the project card block containing the title
    pattern = r'(<div class="project-card[^"]*")([^>]*>[\s\S]*?<h3>' + re.escape(title) + r'</h3>)'
    replacement = r'\1 onclick="openModal(\'' + pid + r'\')"\2'
    html = re.sub(pattern, replacement, html)

# Add Modals before </body>
modals_html = """
    <!-- Modals -->
    <div class="modal-overlay" id="modalOverlay" onclick="closeModal()"></div>
    
    <div class="modal" id="modal-sms">
        <button class="modal-close" onclick="closeModal()">×</button>
        <h3>JCL Safety Management System</h3>
        <p><strong>Case Study:</strong> Developed a complete ISM Code compliance documentation suite containing 110 files. This included 21 fleet PDFs, 22 editable source documents, and 49 operational forms for Section 7.</p>
        <p><strong>Impact:</strong> Standardized safety protocols across the fleet and ensured complete regulatory compliance, minimizing operational risks.</p>
    </div>

    <div class="modal" id="modal-cyber">
        <button class="modal-close" onclick="closeModal()">×</button>
        <h3>Cybersecurity Policy Suite</h3>
        <p><strong>Case Study:</strong> Authored 14 IT security policies along with a comprehensive cybersecurity audit report and remediation roadmap.</p>
        <p><strong>Impact:</strong> Strengthened organizational security posture in alignment with NIST CSF, providing clear incident response and disaster recovery procedures.</p>
    </div>

    <div class="modal" id="modal-it">
        <button class="modal-close" onclick="closeModal()">×</button>
        <h3>IT Infrastructure Portfolio</h3>
        <p><strong>Case Study:</strong> Deployed and managed vessel network installations, CCTV, and Starlink vs 5G systems. Maintained detailed IT asset registers and security audit checklists.</p>
        <p><strong>Impact:</strong> Ensured robust, high-availability connectivity for offshore fleets, vastly improving real-time communication and data transfer.</p>
    </div>

    <div class="modal" id="modal-budget">
        <button class="modal-close" onclick="closeModal()">×</button>
        <h3>Budget Link Integrity Checker</h3>
        <p><strong>Case Study:</strong> Built a 385-line Python automation tool to validate complex Excel workbook chains, checking for external references, missing sheets, and stale named ranges.</p>
        <p><strong>Impact:</strong> Reduced budget calculation errors and saved hours of manual validation time during financial planning.</p>
    </div>

    <div class="modal" id="modal-smartvessel">
        <button class="modal-close" onclick="closeModal()">×</button>
        <h3>SmartVessel Deployment</h3>
        <p><strong>Case Study:</strong> Created the training framework, teleprompter scripts, and user guides for rolling out the SmartVessel software across the entire fleet (Cloud + Local Server).</p>
        <p><strong>Impact:</strong> Accelerated crew onboarding and ensured high adoption rates for the new fleet management system.</p>
    </div>

    <div class="modal" id="modal-papaya">
        <button class="modal-close" onclick="closeModal()">×</button>
        <h3>Papaya Genetic Diversity Research</h3>
        <p><strong>Case Study:</strong> Conducted comprehensive research on 60 Nigerian pawpaw accessions. Used Principal Component Analysis (PCA) and Cluster Analysis to map genetic traits.</p>
        <p><strong>Impact:</strong> Published lead-author paper in the Nigerian Journal of Horticultural Science, demonstrating high heritability of Vitamin C and Carotene for future biofortification.</p>
    </div>

    <div class="modal" id="modal-mcp">
        <button class="modal-close" onclick="closeModal()">×</button>
        <h3>Outlook + OneDrive MCP Server</h3>
        <p><strong>Case Study:</strong> Engineered a custom Model Context Protocol (MCP) server in TypeScript using the Microsoft Graph API.</p>
        <p><strong>Impact:</strong> Empowered AI agents to securely read emails, manage calendars, and access OneDrive files, showcasing advanced AI-native system integration.</p>
    </div>
"""
html = html.replace('</body>', modals_html + '\n</body>')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
