export class ApiClient {
  constructor() {
    this.token = document.querySelector("#app-config").dataset.authToken;
  }

  async fetch(url, options = {}) {
    if (this.authToken) {
      throw new Error("Auth token not found");
    }

    const response = await fetch(url, {
      ...options,
      headers: {
        "X-Auth-Token": this.token,
        ...options.headers,
      },
    });

    if (!response.ok) {
      throw new Error(`HTTP ERROR! Status: ${response.status}`);
    }

    return response.json();
  }
}
