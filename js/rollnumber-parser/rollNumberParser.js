/*
    format:
    <CAMPUS(2)>.<SCHOOL(2)>.<PROGRAMME(1)><DURATION(1)><BRANCH(3)><START_YEAR(2)><ROLL_NO(3)>
*/

const SCHOOL_NAMES = {
  EN: 'Engineering',
  SC: 'Computing',
  AI: 'Artificial Intelligence',
};

const PROGRAMME_TYPES = {
  U: 'Undergraduate',
  P: 'Postgraduate',
  D: 'Doctorate',
  R: 'Research',
};

export function parseRollNumber(rollNumber) {
  const defaultResult = {
    campus: 'Unknown',
    school: 'Unknown',
    programmeType: 'Unknown',
    duration: 0,
    branch: 'Unknown',
    startYear: 0,
    graduationYear: 0,
    rollCall: '',
    isValid: false,
  };

  if (!rollNumber) return defaultResult;

  const cleanRoll = rollNumber.replace(/\./g, '').toUpperCase();

  const match = cleanRoll.match(
    /^([A-Z]{2})([A-Z]{2})([UPDR])([\d*])([A-Z]{3})(\d{2})(\d{3})$/
  );

  if (!match) return defaultResult;

  const [, campus, school, programme, duration, branch, yearDigits, rollCall] = match;

  const programmeType = PROGRAMME_TYPES[programme] || 'Unknown';
  const isIndefinite = duration === '*';
  const durationInt = isIndefinite ? null : parseInt(duration, 10);
  const startYear = 2000 + parseInt(yearDigits, 10);
  const graduationYear = durationInt ? startYear + durationInt : null;

  return {
    campus,
    school: SCHOOL_NAMES[school] || school,
    programmeType,
    duration: durationInt,
    branch,
    startYear,
    graduationYear,
    rollCall,
    isValid: true,
  };
}

export function getGraduationYear(rollNumber) {
  const info = parseRollNumber(rollNumber);
  return info.graduationYear;
}

export function getBatchDisplay(rollNumber) {
  const year = getGraduationYear(rollNumber);
  return year ? `Class of ${year}` : 'N/A';
}

export function getProgrammeDisplay(rollNumber) {
  const info = parseRollNumber(rollNumber);
  if (!info.isValid || info.programmeType === 'Unknown') return 'N/A';
  const duration = info.duration ? `${info.duration}-Year` : 'Indefinite Duration';
  return `${duration} ${info.programmeType}`;
}
