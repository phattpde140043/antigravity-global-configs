// Complete implementation of condition-based waiting utilities

import type { ThreadManager } from '~/threads/thread-manager';
import type { LaceEvent, LaceEventType } from '~/threads/types';

/**
 * Wait for a specific event type to appear in thread
 * 
 * @param threadManager - The thread manager to query
 * @param threadId - Thread to check for events
 * @param eventType - Type of event to wait for
 * @param timeoutMs - Maximum time to wait (default 5000ms)
 * @returns Promise resolving to the first matching event
 * 
 * Example:
 *   await waitForEvent(threadManager, agentThreadId, 'TOOL_RESULT');
 */
export function waitForEvent(
  threadManager: ThreadManager,
  threadId: string,
  eventType: LaceEventType,
  timeoutMs = 5000
): Promise<LaceEvent> {
  return new Promise((resolve, reject) => {
    const startTime = Date.now();
    
    const check = () => {
      const events = threadManager.getEvents(threadId);
      const match = events.find(e => e.type === eventType);
      
      if (match) {
        resolve(match);
        return;
      }
      
      if (Date.now() - startTime > timeoutMs) {
        reject(new Error(`Timeout waiting for event ${eventType} in thread ${threadId}`));
        return;
      }
      
      setTimeout(check, 100);
    };
    
    check();
  });
}

/**
 * Wait for a specific count of events to appear
 * 
 * @param threadManager - The thread manager
 * @param threadId - Thread ID
 * @param count - Expected minimum event count
 * @param timeoutMs - Maximum time to wait
 */
export async function waitForEventCount(
  threadManager: ThreadManager,
  threadId: string,
  count: number,
  timeoutMs = 5000
): Promise<LaceEvent[]> {
  const startTime = Date.now();
  
  while (Date.now() - startTime < timeoutMs) {
    const events = threadManager.getEvents(threadId);
    if (events.length >= count) {
      return events;
    }
    await new Promise(r => setTimeout(r, 100));
  }
  
  throw new Error(`Timeout waiting for ${count} events. Found ${threadManager.getEvents(threadId).length}.`);
}

/**
 * Wait for an event matching a specific predicate
 */
export async function waitForEventMatch(
  threadManager: ThreadManager,
  threadId: string,
  predicate: (e: LaceEvent) => boolean,
  timeoutMs = 5000
): Promise<LaceEvent> {
  const startTime = Date.now();
  
  while (Date.now() - startTime < timeoutMs) {
    const events = threadManager.getEvents(threadId);
    const match = events.find(predicate);
    if (match) return match;
    await new Promise(r => setTimeout(r, 100));
  }
  
  throw new Error(`Timeout waiting for matching event in thread ${threadId}`);
}
