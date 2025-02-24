import { registry } from "@web/core/registry";
const { Component } = owl;

export class CampusDashboard extends Component {
  setup() {
    console.log("Campus Dashboard Loaded");
  }
}
CampusDashboard.template="CampusDashboard"
registry.category("actions").add("campus_dashboard", CampusDashboard);
