import { expect } from 'chai';
import { createQueue } from 'kue';
import createPushNotificationsJobs from './8-job.js';


let queue;

describe('createPushNotificationsJobs', () => {
  before(() => {
    queue = createQueue();
    queue.testMode = true;
  });

  beforeEach(() => {
    queue.clear();
  });
  after(() => {
    queue.testMode = false;
  });

   it('create jobs and add them to the queue', () => {
     const jobs = [
       { phoneNumber: '4153518780', message: 'Test message 1' },
       { phoneNumber: '4153518781', message: 'Test message 2' },
       { phoneNumber: '4153518743', message: 'Test message 3' }
     ];
     createPushNotificationsJobs(jobs, queue);
     const ids = queue.testMode.jobs().map(job => job.id);
     expect(ids).to.have.lengthOf(3);
     jobs.forEach((jobInfo, index) => {
       const job = queue.testMode.jobs()[index];
       expect(job.data.phoneNumber).to.equal(jobInfo.phoneNumber);
       expect(job.data.message).to.equal(jobInfo.message);
     });
   });
});
