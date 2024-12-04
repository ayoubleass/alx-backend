import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);

client.on('connect', () => console.log('Redis client connected to the server'));

client.on('error', (err) => console.error(`Redis client not connected to the server: ${err}`));

const setNewSchool = (schoolName, value) => client.set(schoolName, value, redis.print);

const displaySchoolValue = async (schoolName) => {
  const res = await getAsync(schoolName);
  console.log(res);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
