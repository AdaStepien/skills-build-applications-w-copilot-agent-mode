import React, { useEffect, useState } from 'react';

const Leaderboard = () => {
  const [leaders, setLeaders] = useState([]);
  useEffect(() => {
    const endpoint = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/leaderboard/`;
    console.log('Fetching Leaderboard from:', endpoint);
    fetch(endpoint)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        setLeaders(results);
        console.log('Leaderboard data:', results);
      });
  }, []);
  return (
    <div className="mt-4">
      <h2 className="mb-3">Leaderboard</h2>
      <table className="table table-striped table-bordered">
        <thead className="table-dark">
          <tr>
            <th>Name</th>
            <th>Score</th>
            <th>Rank</th>
          </tr>
        </thead>
        <tbody>
          {leaders.map((leader, idx) => (
            <tr key={leader.id || idx}>
              <td>{leader.name || '-'}</td>
              <td>{leader.score || '-'}</td>
              <td>{leader.rank || idx + 1}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};
export default Leaderboard;
