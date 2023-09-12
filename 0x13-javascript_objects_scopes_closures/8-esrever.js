#!/usr/bin/node
exports.esrever = function (list) {
  const r = [];
  for (const element of list) {
    r.unshift(element);
  }
  return r;
};
