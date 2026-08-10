//lesson 1
export type Mail = {
  from: string;
  to: string[];
  subject: string;
  body: string;
  urgent: boolean;
};

export function processMail(mail: Mail) {
  return `FROM: ${mail.from}
TO: ${mail.to}
SUBJECT: ${mail.urgent ? "[URGENT] " : ""}${mail.subject}
BODY: ${mail.body}`;
}

//lesson 2
export type Mail = {
  from: string;
  to: string[];
  subject: string;
  body: string;
  urgent: boolean;
  cc: string[];
};

// don't touch below this line

export function processMail(mail: Mail) {
  return `FROM: ${mail.from}
TO: ${mail.to.join(", ")}
CC: ${mail.cc.join(",")}
SUBJECT: ${mail.urgent ? "[URGENT] " : ""}${mail.subject}
BODY: ${mail.body}`;
}

//lesson 3
export type Mail = {
  from: string;
  to: string[];
  subject: string;
  body: string;
  urgent: boolean;
  cc?: string[];
};

// don't touch below this line

export function processMail(mail: Mail) {
  return `FROM: ${mail.from}
TO: ${mail.to}${!mail.cc ? "" : "\nCC: " + mail.cc}
SUBJECT: ${mail.urgent ? "[URGENT] " : ""}${mail.subject}
BODY: ${mail.body}`;
}

//lesson 4
export type Address = {
  name: string;
  domain: string;
};

// don't touch below this line

export type Mail = {
  from: Address;
  to: Address[];
  subject: string;
  body: string;
  urgent: boolean;
  cc?: Address[];
};

export function processMail(mail: Mail) {
  let addressees = "";
  for (const addressee of mail.to) {
    addressees += `${addressee.name}@${addressee.domain}, `;
  }
  addressees = addressees.slice(0, -2);

  let copies = "";
  if (mail.cc) {
    copies = "\nCC: ";
    for (const addressee of mail.cc) {
      copies += `${addressee.name}@${addressee.domain}, `;
    }
    copies = copies.slice(0, -2);
  }

  return `FROM: ${mail.from.name}@${mail.from.domain}
TO: ${addressees}${copies}
SUBJECT: ${mail.urgent ? "[URGENT] " : ""}${mail.subject}
BODY: ${mail.body}`;
}

//lesson 5
export type InternalAddress = {
  kind: "internal";
  firstName: string;
  lastName: string;
}

export type ExternalAddress = {
  kind: "external";
  username: string;
  domain: string;
}

// don't touch below this line

export type Address = InternalAddress | ExternalAddress;

export function formatAddresses(addresses: Address[]) {
  let formatted = "";
  for (const address of addresses) {
    if (address.kind === "internal") {
      formatted += `${address.firstName}.${address.lastName}@support.ai, `;
    }
    if (address.kind === "external") {
      formatted += `${address.username}@${address.domain}, `;
    }
  }
  return formatted.slice(0, -2);
}

//lesson 6
export function findNumUniqueLabels(formattedAddresses: string[]) {
  return new Set<string>(formattedAddresses).size;
}

//lesson 7
export function getFileLength(files: Map<string, string>, filename: string) {
  const contents = files.get(filename)
  if (!contents) {
    return 0;
  }
  const bytes = new TextEncoder().encode(contents)
  return bytes.length;
}

//lesson 8
export type MailPreferences = {
  [key: string]: boolean;
};

// don't touch below this line

export function setPreference(
  preferences: MailPreferences,
  key: string,
  value: boolean,
) {
  const exists = key in preferences;
  preferences[key] = value;
  return exists;
}

//lesson 9
export type MailPreferences = {
  [field: string]: string | boolean;
  doNotDisturb: boolean;
  outOfOffice: boolean;
};

// don't touch below this line

export function canContact(preferences: MailPreferences): boolean {
  return !(preferences.doNotDisturb || preferences.outOfOffice);
}

//lesson 10
export const TWO_FACTOR = Symbol("twoFactor");
export const BIOMETRIC_LOCK = Symbol("biometricLock");

export type MailPreferences = {
  [key: PropertyKey]: boolean | string;
  doNotDisturb: boolean;
  outOfOffice: boolean;
  [TWO_FACTOR]: boolean;
  [BIOMETRIC_LOCK]: boolean;
};

// don't touch above this line

export function isSecure(preferences: MailPreferences) {
  return preferences[TWO_FACTOR] || preferences[BIOMETRIC_LOCK];
}

//letter 11
export type MailPreferences = {
  [key: PropertyKey]: boolean | string;
  readonly doNotDisturb: boolean;
  readonly outOfOffice: boolean;
};

//letter 12
export const defaultPreferences = Object.freeze({
  name: "Kreese",
  doNotDisturb: false,
  outOfOffice: false,
});

//letter 13
export type MailPreferences = {
  [key: PropertyKey]: boolean | string;
  doNotDisturb: boolean;
  outOfOffice: boolean;
};

// don't touch above this line

export const newMailPreferences = {
  doNotDisturb: false,
  outOfOffice: false,
  signature: "Boots, Support.ai Wizard Bear",
  theme: "dark",
} satisfies MailPreferences;

//letter 14
export type MailPreferences = {
  [key: PropertyKey]: boolean | string;
  doNotDisturb: boolean;
  outOfOffice: boolean;
};

export function configurePreferences(
  doNotDisturb: boolean,
  outOfOffice: boolean,
): MailPreferences;

export function configurePreferences(
  doNotDisturb: boolean,
  outOfOffice: boolean | string,
  useSystemTheme: boolean,
  theme: string,
): MailPreferences;

// Do not touch below this line

export function configurePreferences(
  doNotDisturb: boolean,
  outOfOffice: boolean | string,
  useSystemTheme?: boolean,
  theme?: string,
): MailPreferences {
  if (typeof outOfOffice === "string") {
    return {
      doNotDisturb: false,
      outOfOffice: false,
      useSystemTheme: doNotDisturb,
      theme: outOfOffice,
    };
  } else if (useSystemTheme !== undefined && theme !== undefined) {
    return {
      doNotDisturb: doNotDisturb,
      outOfOffice: outOfOffice,
      useSystemTheme: useSystemTheme,
      theme: theme,
    };
  } else {
    return {
      doNotDisturb: doNotDisturb,
      outOfOffice: outOfOffice,
    };
  }
}
