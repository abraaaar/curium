
import React from 'react';

class UserDetailsPage extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      username: '', // Assuming username will be retrieved from state or props
      messages: [] // Assuming messages will be retrieved from state or props
    };
  }

  render() {
    const { username, messages } = this.state;

    return (
      <div>
        <div className="headerr">
          <img
            className="logo"
            src="https://media.licdn.com/dms/image/C560BAQExlYi7r4CpWg/company-logo_200_200/0/1663591474302?e=2147483647&v=beta&t=3Mix-eHlRE8yD_x4XNq-B0wGuhSOjtffHssBw5jdvEc"
            alt="Company Logo"
          />
          <h1>Curium Life</h1>
          <h2>Higher Intelligence Safer Surgery</h2>
        </div>
        <nav>
          {username && (
            <>
              <p>Welcome, {username}!</p>
              <a href="#logout">Logout</a>
            </>
          )}
        </nav>
        <div className="field-set">
          <div className="mb-3">
            <form method="post" encType="multipart/form-data">
              <label htmlFor="image" className="form-label">
                Upload Image
              </label>
              <input
                type="file"
                id="image"
                name="image"
                className="form-control"
                required
              />
              <br />
              <button type="submit" className="btn btn-success">
                Next
              </button>
            </form>
          </div>
        </div>

        {messages.length > 0 && (
          <div className="alert alert-success mt-3">
            {messages.map((message, index) => (
              <span key={index}>{message}</span>
            ))}
          </div>
        )}

        {/* Bootstrap JS and dependencies */}
        <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.2/dist/umd/popper.min.js"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
      </div>
    );
  }
}

export default UserDetailsPage;

