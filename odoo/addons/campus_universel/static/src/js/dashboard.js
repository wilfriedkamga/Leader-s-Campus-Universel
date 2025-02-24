import { registry } from "@web/core/registry";
const { Component, useState } = owl;

export class CampusDashboard extends Component {
  setup() {
    this.project_state = useState({
      projects_count: 100,
    });
  }
}
CampusDashboard.template = "CampusDashboard";
registry.category("actions").add("campus_dashboard", CampusDashboard);
