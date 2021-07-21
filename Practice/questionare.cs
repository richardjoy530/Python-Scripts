using System;
using System.Collections.Generic;
using System.Configuration;
using System.Data;
using System.Data.SqlClient;
using System.Linq;
using System.Net;
using System.Net.Http;
using System.Web.Http;
using Questionnaire.Models;
using Questionnaire.Controllers;

namespace Questionnaire.Controllers
{
    public class AddQuestionAnswerController : ApiController
    {
        public string Post(Questions question,Answers_Version answer)
        {
            try
            {
                string query = @"insert into dbo.Questions values('" + question.User_Id + @"','" + question.Category_Id + @"','" + question.Type_Id + @"','" + question.Reference + @"','" + question.Tags + @"')";

                DataTable table = new DataTable();
                using (var con = new SqlConnection(ConfigurationManager.ConnectionStrings["QuestionnaireAppDB"].ConnectionString))
                using (var cmd = new SqlCommand(query, con))
                using (var da = new SqlDataAdapter(cmd))
                {
                    cmd.CommandType = CommandType.Text;
                    da.Fill(table);
                }


                string query2 = @"
                
                IF EXISTS (SELECT Question_Id FROM Answers_Version WHERE  Question_Id = '"+question.Question_Id+ @"')
                begin
                DECLARE  @v int  select @v= max([Version]) from Answers_Version where Question_Id = '" + answer.Question_Id + @"'
                INSERT INTO dbo.Answers_Version VALUES (@v +1,'" + answer.Question_Id + @"','" + answer.Answer_Content + @"','" + answer.Images + @"')
                end
                          
                else 
                INSERT INTO dbo.Answers_Version VALUES(1'" + question.Question_Id + @"','" + answer.Answer_Content + @"','" + answer.Images + @"')";
                
                DataTable table2 = new DataTable();
                using (var con2 = new SqlConnection(ConfigurationManager.ConnectionStrings["QuestionnaireAppDB"].ConnectionString))
                using (var cmd = new SqlCommand(query2, con2))
                using (var da = new SqlDataAdapter(cmd))
                {
                    cmd.CommandType = CommandType.Text;
                    da.Fill(table);
                }

                return "Added Successfully!!";
            }
            catch (Exception)
            {

                return "Failed to Add!!";
            }


        }

        /*
        public string Post(Answers_Version answer)
        {
            try
            {
                /*string query = @"
                    insert into dbo.Answers_Version values('" + answer.Version + @"','" + answer.Question_Id + @"','" + answer.Answer_Content + @"','" + answer.Images + @"')";#1#
                string query = @"IF EXISTS (SELECT Question_Id FROM Answers_Version WHERE  Question_Id = 13)
                                    begin
                                    DECLARE  @v int  select @v= max([Version]) from Answers_Version where Question_Id = 13
                                    INSERT INTO dbo.Answers_Version VALUES (@v +1,13,'" + answer.Answer_Content + @"','" + answer.Images + @"')
                                    end
                          
                        else 
                            INSERT INTO dbo.Answers_Version VALUES(1,10,'" + answer.Answer_Content + @"','" + answer.Images + @"')";
                DataTable table = new DataTable();
                using (var con = new SqlConnection(ConfigurationManager.ConnectionStrings["QuestionnaireAppDB"].ConnectionString))
                using (var cmd = new SqlCommand(query, con))
                using (var da = new SqlDataAdapter(cmd))
                {
                    cmd.CommandType = CommandType.Text;
                    da.Fill(table);
                }
                return "Added Successfully!!";
            }
            catch (Exception)
            {
                return "Failed to Add!!";
            }
        }
        */

    }
}




/*
public HttpResponseMessage Get()
{
    string query = @" select Version,Question_Id,Answer_Content,Images from dbo.Answers_Version";
    //select User_Id, Question_Id, Category_Id, Type_Id, Reference, Tags  from Questions
    DataTable table = new DataTable();
    using (var con = new SqlConnection(ConfigurationManager.ConnectionStrings["QuestionnaireAppDB"].ConnectionString))
    using (var cmd = new SqlCommand(query, con))
    using (var da = new SqlDataAdapter(cmd))
    {
        cmd.CommandType = CommandType.Text;
        da.Fill(table);
    }
    return Request.CreateResponse(HttpStatusCode.OK, table);
}*/