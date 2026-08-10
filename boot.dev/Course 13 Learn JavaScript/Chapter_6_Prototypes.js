//Lesson 1
const notification = {
  notify(recipient, message) {
    return `Notification for ${recipient}: ${message}`;
  },
};

const systemNotification = Object.create(notification);

systemNotification.broadcast = function (message) {
  return `Broadcast to all users: ${message}`
}

// don't touch below this line

export { notification, systemNotification };

//Lesson 2
const user = {
  name: "Default User",
  type: "user",
};

const adminUser = Object.create(user);
adminUser.type = "admin";

function isAdmin (user) {
  return "admin" === Object.getPrototypeOf(user).type;
}

// don't touch below this line

export { user, adminUser, isAdmin };
