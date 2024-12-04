import kue from 'kue';

const queue = kue.createQueue();
const data = {
  phoneNumber: '0620542066',
  message: 'Hello, you have a new notification!',
};

const job = queue.create('push_notification_code', data ).save((err) => {
  if(!err) {
    console.log(`Notification job created: ${job.id}`);
  }
});

job.on('complete', () => {
  console.log('Notification job completed');
});

job.on('failed', (err) => {
  console.log('Notification job failed');
});
