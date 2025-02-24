import { registry } from "@web/core/registry";
import { Component } from "@odoo/owl";

class CampusDashboard extends Component {
  setup() {
    console.log("Campus Dashboard Loaded");
  }
}

registry.category("actions").add("campus_dashboard", CampusDashboard);
