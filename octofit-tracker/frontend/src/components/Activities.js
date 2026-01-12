import React, { useEffect, useState } from 'react';

const Activities = () => {
  const [activities, setActivities] = useState([]);
  useEffect(() => {
    const endpoint = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/activities/`;
    console.log('Fetching Activities from:', endpoint);
    fetch(endpoint)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        setActivities(results);
        console.log('Activities data:', results);
      });
  }, []);
  return (
    <div className="mt-4">
      <h2 className="mb-3">Activities</h2>
      <table className="table table-striped table-bordered">
        <thead className="table-dark">
          <tr>
            <th>Name</th>
            <th>Description</th>
            <th>Date</th>
          </tr>
        </thead>
        <tbody>
          {activities.map((activity, idx) => (
            <tr key={activity.id || idx}>
              <td>{activity.name || '-'}</td>
              <td>{activity.description || '-'}</td>
              <td>{activity.date || '-'}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};
export default Activities;
