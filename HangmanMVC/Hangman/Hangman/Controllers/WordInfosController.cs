using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.Rendering;
using Microsoft.EntityFrameworkCore;
using Hangman.Models;
using Hangman.Persistance;

namespace Hangman.Controllers
{
    public class WordInfosController : Controller
    {
        private readonly HangmanContext _context;

        public WordInfosController(HangmanContext context)
        {
            _context = context;
        }

        // GET: WordInfos
        public async Task<IActionResult> Index()
        {
            var hangmanContext = _context.WordInfos.Include(w => w.Language).Include(w => w.Submitter);
            return View(await hangmanContext.ToListAsync());
        }

        // GET: WordInfos/Details/5
        public async Task<IActionResult> Details(int? id)
        {
            if (id == null)
            {
                return NotFound();
            }

            var wordInfo = await _context.WordInfos
                .Include(w => w.Language)
                .Include(w => w.Submitter)
                .FirstOrDefaultAsync(m => m.WordId == id);
            if (wordInfo == null)
            {
                return NotFound();
            }

            return View(wordInfo);
        }

        // GET: WordInfos/Create
        public IActionResult Create()
        {
            ViewData["LanguageId"] = new SelectList(_context.Languages, "LanguageId", "LanguageName");
            ViewData["SubmitterId"] = new SelectList(_context.Users, "UserId", "Mail");
            return View();
        }

        // POST: WordInfos/Create
        // To protect from overposting attacks, please enable the specific properties you want to bind to, for 
        // more details see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Create([Bind("WordId,Word,IsApproved,DateSubmitted,SubmitterId,LanguageId")] WordInfo wordInfo)
        {
            if (ModelState.IsValid)
            {
                _context.Add(wordInfo);
                await _context.SaveChangesAsync();
                return RedirectToAction(nameof(Index));
            }
            ViewData["LanguageId"] = new SelectList(_context.Languages, "LanguageId", "LanguageName", wordInfo.LanguageId);
            ViewData["SubmitterId"] = new SelectList(_context.Users, "UserId", "Mail", wordInfo.SubmitterId);
            return View(wordInfo);
        }

        // GET: WordInfos/Edit/5
        public async Task<IActionResult> Edit(int? id)
        {
            if (id == null)
            {
                return NotFound();
            }

            var wordInfo = await _context.WordInfos.FindAsync(id);
            if (wordInfo == null)
            {
                return NotFound();
            }
            ViewData["LanguageId"] = new SelectList(_context.Languages, "LanguageId", "LanguageName", wordInfo.LanguageId);
            ViewData["SubmitterId"] = new SelectList(_context.Users, "UserId", "Mail", wordInfo.SubmitterId);
            return View(wordInfo);
        }

        // POST: WordInfos/Edit/5
        // To protect from overposting attacks, please enable the specific properties you want to bind to, for 
        // more details see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Edit(int id, [Bind("WordId,Word,IsApproved,DateSubmitted,SubmitterId,LanguageId")] WordInfo wordInfo)
        {
            if (id != wordInfo.WordId)
            {
                return NotFound();
            }

            if (ModelState.IsValid)
            {
                try
                {
                    _context.Update(wordInfo);
                    await _context.SaveChangesAsync();
                }
                catch (DbUpdateConcurrencyException)
                {
                    if (!WordInfoExists(wordInfo.WordId))
                    {
                        return NotFound();
                    }
                    else
                    {
                        throw;
                    }
                }
                return RedirectToAction(nameof(Index));
            }
            ViewData["LanguageId"] = new SelectList(_context.Languages, "LanguageId", "LanguageName", wordInfo.LanguageId);
            ViewData["SubmitterId"] = new SelectList(_context.Users, "UserId", "Mail", wordInfo.SubmitterId);
            return View(wordInfo);
        }

        // GET: WordInfos/Delete/5
        public async Task<IActionResult> Delete(int? id)
        {
            if (id == null)
            {
                return NotFound();
            }

            var wordInfo = await _context.WordInfos
                .Include(w => w.Language)
                .Include(w => w.Submitter)
                .FirstOrDefaultAsync(m => m.WordId == id);
            if (wordInfo == null)
            {
                return NotFound();
            }

            return View(wordInfo);
        }

        // POST: WordInfos/Delete/5
        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> DeleteConfirmed(int id)
        {
            var wordInfo = await _context.WordInfos.FindAsync(id);
            _context.WordInfos.Remove(wordInfo);
            await _context.SaveChangesAsync();
            return RedirectToAction(nameof(Index));
        }

        private bool WordInfoExists(int id)
        {
            return _context.WordInfos.Any(e => e.WordId == id);
        }
    }
}
